---
name: feishu-doc-best-practices
description: 飞书文档创建和权限管理的最佳实践。用于：1) 创建飞书文档时避免空内容bug；2) 处理文档权限问题；3) 排查飞书API调用失败。
---

# 飞书文档操作最佳实践

## 核心原则

### 1. 创建文档时

**不要**使用 `content` 参数创建文档（会创建空文档）

**正确做法**：
1. 用 `create` 只传 `title` 参数
2. 立即用 `append` 追加内容

```typescript
// ❌ 错误
feishu_doc(action="create", content="# 标题\n内容", title="文档")

// ✅ 正确
feishu_doc(action="create", title="文档")
feishu_doc(action="append", content="# 标题\n内容", doc_token="获取到的token")
```

### 2. 权限问题

飞书机器人创建的文档默认没有用户权限。

**当前已知方案**：
- 配置 `perm: true`（可能不生效）
- 用户手动在飞书点击"分享"添加权限

**不要**承诺能自动解决权限问题（当前OpenClaw版本可能不支持）

### 3. 排查问题

| 问题 | 排查步骤 |
|------|----------|
| 文档为空 | 用 append 修复 |
| 权限失败 | 查 feishu_perm 工具是否启用 |
| API报错 | 查看返回的错误信息 |

## 常见错误

- `requester_permission_added: false` → 权限添加失败，手动处理
- `create` 返回空内容 → 立即用 append 追加

## 参考文档

- 飞书开放平台：https://open.feishu.cn/document/
