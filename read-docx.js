const fs = require('fs');
const path = require('path');

// 用 mammoth 更适合提取纯文本
const mammoth = require('mammoth');

const docxPath = 'C:\\Users\\danie\\.openclaw\\media\\outbound\\95ad2ec5-59e9-4055-b06e-4622519bbe2d.docx';

async function extractText() {
  try {
    const result = await mammoth.extractRawText({ path: docxPath });
    console.log(result.value);
  } catch (err) {
    console.error('Error:', err.message);
  }
}

extractText();
