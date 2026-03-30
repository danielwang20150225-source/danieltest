# OpenClaw 常用命令整理

## 基础命令

| 命令 | 说明 |
|------|------|
| `openclaw --help` | 显示帮助 |
| `openclaw --version` | 查看版本 |
| `openclaw setup` | 初始化配置 |

## 网关管理

| 命令 | 说明 |
|------|------|
| `openclaw gateway start` | 启动网关 |
| `openclaw gateway stop` | 停止网关 |
| `openclaw gateway status` | 查看状态 |
| `openclaw gateway restart` | 重启网关 |
| `openclaw gateway --port 18789` | 指定端口启动 |

## 消息发送

| 命令 | 说明 |
|------|------|
| `openclaw message send --target xxx --message "内容"` | 发送消息 |
| `openclaw channels login` | 登录频道 |

## 模型管理

| 命令 | 说明 |
|------|------|
| `openclaw models list` | 列出可用模型 |
| `openclaw models --help` | 模型帮助 |

## 健康检查

| 命令 | 说明 |
|------|------|
| `openclaw health` | 检查网关健康状态 |
| `openclaw doctor` | 诊断并修复问题 |

## 文档

| 命令 | 说明 |
|------|------|
| `openclaw docs` | 打开文档 |

## 其他

| 命令 | 说明 |
|------|------|
| `openclaw tui` | 打开终端UI |
| `openclaw dashboard` | 打开控制面板 |
| `openclaw logs` | 查看日志 |

---

*整理于 2026-03-12*
