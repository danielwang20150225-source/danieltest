# OpenClaw 使用心得与技巧

> 整理日期：2026-03-12

---

## 一、什么是 OpenClaw？

OpenClaw 是一个**自托管的AI网关**，连接各种聊天应用（WhatsApp、Telegram、Discord、iMessage等）到AI助手。

**核心理念**：
- 自己掌控数据，不依赖托管服务
- 多渠道统一入口
- 支持Coding Agent + 工具调用 + 记忆 + 多Agent路由

---

## 二、核心概念

### 1. Gateway（网关）
- 核心进程，所有连接的枢纽
- 默认端口：19000（生产）或 19001（开发）
- 控制面板：http://127.0.0.1:18789/

### 2. Channel（渠道）
- 支持：WhatsApp、Telegram、Discord、iMessage、飞书等
- 可以同时连接多个渠道

### 3. Agent（代理）
- 默认使用Pi模型
- 可配置其他LLM（Claude、GPT、Deepseek等）

### 4. Node（节点）
- iOS/Android设备配对
- 支持相机、屏幕、语音功能

---

## 三、常用命令

### 快速启动
```bash
# 安装
npm install -g openclaw@latest

# 初始化
openclaw setup

# 启动网关
openclaw gateway start
# 或指定端口
openclaw gateway --port 18789
```

### 渠道管理
```bash
# 登录渠道
openclaw channels login

# 查看状态
openclaw status
```

### 健康检查
```bash
openclaw health
openclaw doctor
```

---

## 四、使用场景

### 场景1：个人AI助手
- 通过微信/Telegram/Discord随时召唤AI
- 发送消息 → AI响应

### 场景2：开发辅助
- 本地运行代码
- 浏览器自动化
- 文件操作

### 场景3：产品开发
- 像今天开发的"魔法简历"项目
- 完整的前后端开发能力

### 场景4：自动化工作流
- 定时任务（cron）
- 消息推送
- 设备控制（配对手机后）

---

## 五、技巧与最佳实践

### 1. 保持网关运行
- 电脑休眠前注意保存状态
- 长时间运行建议用服务器部署

### 2. 多渠道配置
- 可以同时配置微信、Telegram等多个入口
- 不同渠道可有不同权限

### 3. 记忆功能
- MEMORY.md：长期记忆
- memory/：每日记录
- AGENTS.md：项目规范

### 4. 技能（Skills）
- 可扩展的工具集
- 位置：~/.openclaw/skills/

### 5. 安全配置
- 配置允许的用户列表
- 群聊需要@提及

---

## 六、限制与注意事项

| 注意事项 | 说明 |
|----------|------|
| 电脑需要联网 | 我才能响应 |
| 电脑不能休眠 | 休眠后服务中断 |
| API Key | 需要自备LLM提供商的Key |
| 网络环境 | 部分渠道需要代理 |

---

## 七、官方资源

- 官网：https://openclaw.ai
- 文档：https://docs.openclaw.ai
- Discord：https://discord.com/invite/clawd
- GitHub：https://github.com/openclaw/openclaw

---

*整理于 2026-03-12*
