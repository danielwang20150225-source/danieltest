---
name: mcp-debug
description: MCP（Model Context Protocol）服务调试和问题排查。用于：1) 检查MCP服务是否安装；2) 配置MCP服务器到OpenClaw；3) 排查MCP连接问题。
---

# MCP服务调试指南

## 快速检查

### 1. 检查本地MCP包

```bash
npm list -g --depth=0 | findstr mcp
```

### 2. 检查OpenClaw配置

配置文件路径：`~/.openclaw/openclaw.json`

查找 `mcpServers` 字段。

### 3. 测试MCP服务

尝试直接运行：
```bash
node <mcp包路径>/dist/cli.js --help
```

## 常见问题

### 问题1：mcpServers配置被拒绝

**症状**：配置文件中添加 `mcpServers` 后报错 "Unrecognized key"

**原因**：当前OpenClaw版本可能不支持用户配置的MCP服务器

**处理**：
1. 移除 `mcpServers` 配置
2. 查官方文档确认支持情况
3. 向官方提feature request

### 问题2：ClawHub安装限流

**症状**：`Rate limit exceeded`

**处理**：
1. 等待几分钟后重试
2. 不要连续多次尝试

### 问题3：MCP服务无法启动

**检查**：
1. Node.js是否安装
2. 依赖是否完整
3. 端口是否被占用

## 配置示例

如果OpenClaw支持MCP，配置格式：

```json
{
  "mcpServers": {
    "服务名": {
      "command": "node",
      "args": ["路径/to/mcp-server.js"]
    }
  }
}
```

## 参考资源

- OpenClaw文档：https://docs.openclaw.ai
- MCP协议：https://modelcontextprotocol.io
