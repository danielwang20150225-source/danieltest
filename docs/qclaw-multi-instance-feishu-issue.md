# Qclaw 多实例飞书机器人配置问题分析报告

**日期**: 2026-03-17  
**用户**: Daniel  
**问题**: 在Qclaw客户端模式下配置多OpenClaw实例，每个实例绑定独立的飞书机器人

---

## 一、问题背景

用户希望在Qclaw桌面客户端中运行两个独立的OpenClaw实例：
1. **主实例 (虾仁)** - 处理日常对话
2. **投资实例 (投资虾)** - 处理投资相关问题

每个实例需要绑定独立的飞书机器人账号。

---

## 二、配置情况

### 2.1 主实例配置 (openclaw.json)
```json
{
  "channels": {
    "feishu": {
      "appId": "cli_a925c0f867785cca",
      "appSecret": "RnVEo4ogz3hTILw8LtRrnUZe6tXjrP2q"
    }
  }
}
```

### 2.2 投资实例配置 (openclaw-investing.json)
```json
{
  "channels": {
    "feishu": {
      "appId": "cli_a9320ef630799bca",
      "appSecret": "loHbJW1UuClLtiVuAmbDHfw5DoZQngMG"
    }
  },
  "gateway": {
    "mode": "local",
    "auth": {
      "mode": "token",
      "token": "qclaw-investing-abc123xyz789"
    }
  }
}
```

---

## 三、问题表现

### 3.1 现象描述
- 投资虾Gateway启动后，无法收到飞书消息
- 用户通过投资虾的飞书机器人发送消息，没有响应
- 日志显示消息被主实例（虾仁）接收

### 3.2 日志分析
```
# 投资虾Gateway日志
feishu[default]: bot open_id resolved: ou_9f28a0804c5e0c73720bfd30a1b90671

# 主Gateway日志  
feishu[default]: DM from ou_xxx: 消息内容
feishu[default]: dispatching to agent (session=agent:main:main)
```

**核心问题**: 两个Gateway使用了同一个飞书机器人 (`ou_9f28a0804c5e0c73720bfd30a1b90671`)，这是投资虾应该使用的机器人ID，但主Gateway也在使用它。

---

## 四、调试过程

### 4.1 第一步：检查配置是否存在
- 检查 `openclaw-investing.json` 存在 ✅
- 检查配置内容正确 ✅

### 4.2 第二步：检查Gateway端口
- 主Gateway: 18789/18790
- 投资Gateway: 19003/19004
- 端口都有进程监听 ✅

### 4.3 第三步：尝试用环境变量启动
```bash
$env:OPENCLAW_CONFIG="C:\Users\danie\.openclaw\openclaw-investing.json"
openclaw gateway --port 19003
```

**结果**: Gateway启动成功，但仍然使用了错误的飞书机器人

### 4.4 第四步：检查日志中的机器人ID
- 投资虾Gateway显示: `ou_9f28a0804c5e0c73720bfd30a1b90671`
- 这是投资虾应该使用的机器人 ✅
- 但主Gateway也在接收消息，说明机器人被共享了 ❌

### 4.5 第五步：尝试停止所有Gateway重新启动
- 停止投资虾Gateway
- 重新启动主Gateway
- 检查主Gateway使用的机器人ID

### 4.6 发现根本原因
- **Qclaw客户端可能有内置配置**
- 环境变量 `OPENCLAW_CONFIG` 没有被正确传递
- 或者Qclaw的Gateway启动逻辑覆盖了用户的配置文件

---

## 五、深度分析

### 5.1 Qclaw客户端架构推测
Qclaw客户端可能：
1. 有自己的默认配置文件
2. 内置了飞书机器人配置
3. 不支持或没有正确处理 `OPENCLAW_CONFIG` 环境变量
4. Gateway启动时使用了内置配置而非用户配置

### 5.2 可能的技术原因
1. **配置文件加载顺序问题**
   - Qclaw内置配置 > 环境变量 > 用户配置文件

2. **飞书机器人绑定问题**
   - 飞书机器人只支持一个WebSocket连接
   - 当主Gateway连接后，投资虾无法再连接同一个机器人

3. **Channel配置冲突**
   - Qclaw可能只支持单一飞书Channel配置
   - 多实例无法独立配置飞书

---

## 六、官方优化建议

### 6.1 配置文件透明度
- **建议**: 在Gateway启动日志和Dashboard中明确显示当前使用的配置文件路径
- **当前问题**: 用户无法确认配置文件是否被正确加载

### 6.2 多飞书机器人支持
- **建议**: 支持在同一Gateway中配置多个飞书账号，并通过agent路由区分
- **当前问题**: 只能配置一个飞书Channel

### 6.3 环境变量支持
- **建议**: 明确文档说明如何在Qclaw环境中使用 `OPENCLAW_CONFIG` 或类似机制加载不同配置
- **当前问题**: 环境变量可能不生效或被覆盖

### 6.4 多实例启动机制
- **建议**: 提供更简便的多实例启动方式，如：
  ```bash
  openclaw gateway --config openclaw-investing.json --port 19003
  ```
- **当前问题**: 需要手动设置环境变量，操作繁琐

### 6.5 GUI配置界面
- **建议**: 在Qclaw GUI中添加实例管理功能
  - 可以添加、删除、启动/停止多个OpenClaw实例
  - 每个实例可以独立配置飞书机器人
  - 直观显示每个实例的状态

### 6.6 错误提示优化
- **建议**: 当检测到飞书机器人被其他连接占用时，给出更明确的错误提示
- **当前问题**: 消息静默失败，用户不知道原因

---

## 七、临时解决方案

### 7.1 方案一：切换主实例飞书配置
1. 停止所有Gateway
2. 修改主实例配置，使用另一个飞书机器人
3. 投资虾使用原来的机器人
4. 重新启动两个实例

### 7.2 方案二：等待官方更新
- 向官方反馈此问题
- 等待官方添加多飞书机器人支持

---

## 八、总结

本次调试暴露了Qclaw客户端在**多实例飞书配置**场景下的几个关键问题：

1. **配置加载不透明** - 用户无法确认配置文件是否被正确加载
2. **多飞书机器人不支持** - 无法在同一设备上运行多个使用不同飞书机器人的实例
3. **缺乏明确的错误提示** - 问题发生时用户难以定位原因

建议官方重点优化以上三个方面，提升多实例配置的使用体验。

---

*报告生成时间: 2026-03-17 16:51*
