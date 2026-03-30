# Gateway Watchdog Skill

## 定位
安全重启 OpenClaw Gateway 的标准流程。解决 Gateway 重启会导致 exec 调用断连的问题。

## 工作原理
1. 用 `schtasks` 在**外部**结束并重启 `\OpenClaw Gateway` 定时任务
2. Gateway 在独立进程重启，不影响当前 exec 执行环境
3. 轮询等待 gateway 恢复（默认最多 20×5s = 100s）
4. 返回后 exec 调用正常继续

## 使用场景
- 配置变更需要重启 Gateway
- 定时清理内存/重置状态
- 任何需要重启 gateway 但不希望断 session 的情况

## 调用方式
```bash
powershell -ExecutionPolicy Bypass -File "C:\Users\danie\.openclaw\workspace\scripts\gateway-watchdog.ps1" -WaitSeconds 10 -MaxRetries 20
```

## 参数
- `WaitSeconds`: 首次等待秒数（默认15），gateway 启动后等待多久开始探测
- `MaxRetries`: 最大重试次数（默认20），每次间隔5秒

## 注意
- 不要直接调用 `openclaw gateway restart`，这会杀掉 exec 进程
- Gateway 重启期间 RPC probe 会短暂失败，这是正常的
- 重启后原 session 会自动恢复，不需要手动重连
