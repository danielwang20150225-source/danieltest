# 项目文件规划

## 当前文件位置

| 内容 | 当前位置 | 是否可移 |
|------|----------|----------|
| 项目代码 | C:\Users\danie\.openclaw\workspace\magic-resume | ✅ 可移 |
| 依赖(node_modules) | 项目目录下 | ✅ 随项目移动 |
| npm缓存 | C:\Users\danie\AppData\npm-cache | ⚠️ 需配置 |
| 临时文件 | C:\Users\danie\AppData\Local\Temp | ⚠️ 需配置 |

---

## 规划方案

### 方案：项目整体移到D盘

**新位置**：D:\Projects\magic-resume

**优点**：
- 项目代码在D盘
- node_modules在D盘
- 不占用C盘空间

### npm缓存迁移

```bash
# 设置npm缓存到D盘
npm config set cache "D:\npm-cache"

# 或创建.npmrc文件
```

---

## 需要你确认

1. 是否把项目移到 D:\Projects\magic-resume？
2. 是否需要我帮你配置npm缓存到D盘？

确认后我执行移动操作。