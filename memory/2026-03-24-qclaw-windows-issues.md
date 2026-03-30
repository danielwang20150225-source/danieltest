# Qclaw Windows 平台问题汇总

> 搜索日期：2026-03-24
> 来源：GitHub Issues

---

## 一、主要问题列表

### 1. 微信无法接收消息（高频问题）

**问题描述**：
- 微信插件 (wechat-access) 无法接收消息
- 能正常发送消息，但收不到任何消息
- wechat_messages 表始终为空
- 无接收事件输出

**环境**：
- OS: Windows 11 (NT 10.0.26200)
- OpenClaw: 最新版
- QClaw: 最新版
- WeChat: 3.9.x

**相关 Issue**：
- #52914 - 微信扫码登录后空白页面
- #50899 - 微信插件无法接收消息
- #51497 - 微信消息接收问题
- #50893 - 微信相关问题

---

### 2. 微信扫码登录白屏

**问题描述**：
- 在 QClaw 设置中扫描微信连接二维码后，iPhone 微信显示空白白屏
- 强制杀死微信进程才能恢复
- 退出登录后重新登录问题依旧

**根因**：
检查 config.get 发现，微信集成的两个必需环境变量未注入：
- `channels.wechat-access.guid` - 缺少环境变量 `QCLAW_USER_GUID`
- `channels.wechat-access.userId` - 缺少环境变量 `QCLAW_USER_ID`

两个值始终是未解析的占位符 (`${QCLAW_USER_GUID}` 和 `${QCLAW_USER_ID}`)

---

### 3. 重复安装 OpenClaw

**问题描述**：
- 用户已安装小龙虾 (OpenClaw) 并修改了默认端口
- 安装 QClaw 时没有提示是否使用已有小龙虾
- 观察目录发现重新安装了一套

**相关 Issue**：#52299

---

### 4. qclaw-skip-invite 脚本问题

**问题描述**：
- 在 Windows 上运行 `npx qclaw-skip-invite` 时
- 脚本无法自动关闭正在运行的 QClaw 进程
- 导致后续步骤失败（app.asar 被占用，无法替换）

**相关 Issue**：#7 (haroldneo/OpenQClaw)

---

### 5. 微信远程功能失效

**问题描述**：
- 手动关闭 QClaw 后运行补丁脚本
- 修补显示成功
- 重新打开 QClaw 时应用无法微信远程

**相关 Issue**：#9, #10 (PeanutSplash/qclaw-skip-invite)

---

## 二、解决方案汇总

| 问题 | 可能的解决方案 |
|------|----------------|
| 微信无法接收消息 | 等待官方修复 / 关注 Issue #50899 |
| 微信扫码白屏 | 等待官方修复 / 检查环境变量配置 |
| 重复安装 OpenClaw | 手动指定已有 OpenClaw 路径 |
| 脚本无法关闭进程 | 手动关闭 QClaw 后再运行脚本 |
| 微信远程失效 | 尝试重新安装或联系官方 |

---

## 三、官方渠道

- **官网**：https://qclawai.com
- **GitHub Issues**：https://github.com/openclaw/openclaw/issues
- **Discord 社区**：https://discord.com/invite/clawd
- **微信公众号**：秋芝 AI（评论区图中有二维码）

---

## 四、注意事项

1. **Qclaw 目前仅支持 macOS**（官网明确显示 Windows 敬请期待）
2. Windows 版可能是非官方版本或内部测试版
3. 微信插件问题在 Windows 上反馈较多，可能是平台兼容性问题

---

*待更新...*
