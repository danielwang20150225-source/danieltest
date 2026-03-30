const axios = require('axios');

const APP_ID = 'cli_a925c0f867785cca';
const APP_SECRET = 'RnVEo4ogz3hTILw8LtRrnUZe6tXjrP2q';
const DOC_ID = 'EzfadPw9poDjFNxMZigcZHsSnnb';
const YOUR_OPEN_ID = 'ou_0e0a80c4361f24e4d431bf7b838ec802';

async function getTenantToken() {
  const url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal';
  const resp = await axios.post(url, { app_id: APP_ID, app_secret: APP_SECRET });
  return resp.data.tenant_access_token;
}

async function addPermission(token, docId, openId) {
  const url = 'https://open.feishu.cn/open-apis/drive/v1/permission_members';
  const headers = { 
    Authorization: `Bearer ${token}`,
    'Content-Type': 'application/json'
  };
  const payload = {
    token: docId,
    type: 'docx',
    members: JSON.stringify([{
      open_id: openId,
      perm: 'edit'
    }])
  };
  const resp = await axios.post(url, payload, { headers });
  return resp.data;
}

async function main() {
  try {
    console.log('1. 获取 tenant token...');
    const token = await getTenantToken();
    console.log('✓ token获取成功');
    
    console.log('2. 添加权限...');
    const result = await addPermission(token, DOC_ID, YOUR_OPEN_ID);
    console.log('✓ 结果:', JSON.stringify(result, null, 2));
  } catch (err) {
    console.error('❌ 错误:', err.response?.data || err.message);
  }
}

main();
