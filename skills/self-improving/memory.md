# HOT Memory — Template

> This file is created in `~/self-improving/memory.md` when you first use the skill.
> Keep it ≤100 lines. Most-used patterns live here.

## Example Entries

```markdown
## Preferences
- Code style: Prefer explicit over implicit
- Communication: Direct, no fluff
- Time zone: Asia/Shanghai

## Patterns (promoted from corrections)
- Always use TypeScript strict mode
- Prefer pnpm over npm
- Format: ISO 8601 for dates
- **收到 Token/Key/密码 → 立即写入 MEMORY.md，不依赖会话记录**
- **敏感信息不写入任何文件（包括 MEMORY.md commit），只用环境变量**
- **绝不调用 `openclaw gateway restart`，用 `scripts/gateway-watchdog.ps1`**

## GitHub 协作规范
- `.gitignore` 是必须项，不能让 node_modules 进版本控制
- commit 前检查是否有敏感信息（token、key、password）
- 优先用 clawhub 搜索 skills，npx skills 验证存在后再用
- 安装 skill 后立即 `ls skills/` 验证是否真的存在

## Project defaults
- Tests: Jest with coverage >80%
- Commits: Conventional commits format
- Gateway 重启：走 watchdog 脚本，不走 exec 内部命令
```

## Usage

The agent will:
1. Load this file on every session
2. Add entries when patterns are used 3x in 7 days
3. Demote unused entries to WARM after 30 days
4. Never exceed 100 lines (compacts automatically)
