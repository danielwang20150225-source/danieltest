const html2canvas = require('html2canvas');
const fs = require('fs');

async function capture() {
  // 读取HTML内容并创建一个简单的DOM环境
  const html = fs.readFileSync('openclaw-note.html', 'utf8');
  
  // 由于无法直接在Node中渲染，我们生成一个说明
  console.log('请在浏览器中打开: openclaw-note.html');
  console.log('然后使用浏览器截图功能生成图片');
  console.log('或者可以安装 puppeteer 来自动截图');
}

// 运行
capture().catch(console.error);
