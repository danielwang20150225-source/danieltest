# TOOLS.md - 工具使用规范
# 类比：工具使用手册
# 职责：该怎么用工具？工具列表、使用原则、受限工具说明

## 核心理念

工具是解决问题的手段，不是目的。**用最少的工具解决问题是本事。**

---

## 常用工具选择原则

### 文件操作

| 场景 | 推荐工具 |
|------|----------|
| 读取文件内容 | `read` |
| 创建/覆盖文件 | `write` |
| 精确修改 | `edit` |
| 执行命令/脚本 | `exec` |

**原则**：
- 优先用 `read/write/edit`，少用 `exec` 里的 `cat/echo`
- 路径操作用相对路径，避免硬编码
- 批量修改前先 read 确认，不要盲目写入

### 浏览器操作

| 场景 | 推荐工具 |
|------|----------|
| 自动化操作（填表、点击） | `browser` |
| 只是给用户看网页 | `exec` + `shell:openExternal` |

**原则**：
- 需要交互用 `browser`
- 只是展示URL给用户看，用 `shell:openExternal` 更简单

### 信息获取

| 场景 | 推荐工具 |
|------|----------|
| 网页内容提取 | `web_fetch` |
| 搜索信息 | `web_search` |
| 读YouTube字幕 | `youtube-watcher` |
| 读飞书文档 | `feishu_doc` |

---

## ⚠️ 受限操作 - 需要先确认

以下操作在执行前**必须先问用户**：

1. **删除操作**：文件删除、数据库删除
2. **外部动作**：发邮件、发推特、發布内容
3. **高风险命令**：格式化、删除大量文件
4. **付费操作**：调用需要付费的API

**确认话术**：
> "要执行XXX，这会YYY，确定继续？"

---

## 🔴 雷区 - 绝对不要这样做

### 1. 重复犯错

- 犯过的错误要记住
- 同样的问题不要再用同样的失败方法解决
- 如果之前某条路走不通，换一条路试试

### 2. 车轱辘话

- 不要翻来覆去说同样的话
- 同样的解释最多说一遍
- 直接给结果，不要铺垫太多

### 3. 穷举后再问

- 遇到问题先尝试5-10种方法
- 试了一两个不行就放弃是不行的
- 至少穷举到没有办法为止，再来问我

**错误示范**：
> "这个API调用失败了，你要不要自己试试别的方法？"

**正确示范**：
> "API A失败了，我试试API B...B也挂了，我试试C...都不行，我需要你的API key来调试"

### 4. 过度引导用户

- 不要频繁问"你确定吗？"
- 给选项而不是只问问题
- 能帮用户做决定的就直接做

---

## 💡 好的实践

1. **记住偏好**：用户的偏好要记在脑子里，用在每次回复中
2. **一次说完**：能一次给的信息不要分多次
3. **主动补全**：用户说一半的，你帮忙补全
4. **验证后再报**：说"我试试"的时候，真的去试了再回复结果

---

## Qclaw 特定工具

### uv (Python)

- `uv` 已在 PATH 中
- 运行脚本：`uv run python <script>`
- 安装包：`uv pip install <package>`

### Browser

- `browser` 提供完整自动化（抓取、表单填写、测试）
- 流程：`start` → `snapshot` → `act`
- 开新标签页：`open` + `targetUrl`

---

*最后更新：2026-03-23*

<!-- qclaw:begin -->
## Qclaw Tool Notes

### uv (Python)

- `uv` is bundled with Qclaw and on PATH. Do NOT use bare `python` or `pip`.
- Run scripts: `uv run python <script>` | Install packages: `uv pip install <package>`

### Browser

- `browser` tool provides full automation (scraping, form filling, testing) via an isolated managed browser.
- Flow: `action="start"` → `action="snapshot"` (see page + get element refs like `e12`) → `action="act"` (click/type using refs).
- Open new tabs: `action="open"` with `targetUrl`.
- To just open a URL for the user to view, use `shell:openExternal` instead.
<!-- qclaw:end -->
