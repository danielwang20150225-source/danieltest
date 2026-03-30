// OpenClaw MCP Server
// 让 Cursor 可以调用 OpenClaw 的能力

const { spawn } = require('child_process');

const OPENCLAW_PORT = process.env.OPENCLAW_PORT || 18789;

// 工具列表
const tools = [
  {
    name: "openclaw_browser_navigate",
    description: "在夸克浏览器中打开指定URL",
    inputSchema: {
      type: "object",
      properties: {
        url: { type: "string", description: "要打开的网址" }
      },
      required: ["url"]
    }
  },
  {
    name: "openclaw_browser_snapshot",
    description: "获取当前浏览器页面内容",
    inputSchema: {
      type: "object",
      properties: {}
    }
  },
  {
    name: "openclaw_message_send",
    description: "发送飞书消息",
    inputSchema: {
      type: "object",
      properties: {
        message: { type: "string", description: "要发送的消息内容" }
      },
      required: ["message"]
    }
  }
];

// 执行命令行
function execCommand(cmd) {
  return new Promise((resolve, reject) => {
    const child = spawn('cmd.exe', ['/c', cmd], {
      shell: true,
      env: { ...process.env }
    });
    
    let stdout = '';
    let stderr = '';
    
    child.stdout.on('data', (data) => { stdout += data; });
    child.stderr.on('data', (data) => { stderr += data; });
    
    child.on('close', (code) => {
      if (code === 0) {
        resolve(stdout);
      } else {
        reject(new Error(stderr || `Command failed with code ${code}`));
      }
    });
  });
}

// 处理工具调用
async function callTool(name, args) {
  switch (name) {
    case "openclaw_browser_navigate": {
      // 使用 browser 工具
      const result = await execCommand(`openclaw browser --profile quark navigate "${args.url}"`);
      return { success: true, result };
    }
    
    case "openclaw_browser_snapshot": {
      const result = await execCommand('openclaw browser --profile quark snapshot');
      return { success: true, result };
    }
    
    case "openclaw_message_send": {
      const result = await execCommand(`openclaw message send --message "${args.message}"`);
      return { success: true, result };
    }
    
    default:
      return { success: false, error: `Unknown tool: ${name}` };
  }
}

// MCP 协议处理
process.stdin.setEncoding('utf8');

let buffer = '';

process.stdin.on('data', (chunk) => {
  buffer += chunk;
  
  let newlineIndex;
  while ((newlineIndex = buffer.indexOf('\n')) !== -1) {
    const line = buffer.slice(0, newlineIndex);
    buffer = buffer.slice(newlineIndex + 1);
    
    if (!line.trim()) continue;
    
    try {
      const request = JSON.parse(line);
      handleRequest(request);
    } catch (e) {
      console.error("Parse error:", e);
    }
  }
});

function handleRequest(request) {
  const { id, method, params } = request;
  
  if (method === "tools/list") {
    sendResponse(id, { tools });
  } 
  else if (method === "tools/call") {
    const { name, arguments: args } = params;
    callTool(name, args || {}).then(result => {
      sendResponse(id, { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] });
    }).catch(err => {
      sendResponse(id, { content: [{ type: "text", text: `Error: ${err.message}` }] });
    });
  }
  else if (method === "resources/list") {
    sendResponse(id, { resources: [] });
  }
  else if (method === "resources/read") {
    sendResponse(id, { contents: [] });
  }
}

function sendResponse(id, result) {
  console.log(JSON.stringify({ jsonrpc: "2.0", id, result }));
}

console.error("OpenClaw MCP Server started on port", OPENCLAW_PORT);
