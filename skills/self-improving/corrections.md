# Corrections Log — Template

> This file is created in `~/self-improving/corrections.md` when you first use the skill.
> Keeps the last 50 corrections. Older entries are evaluated for promotion or archived.

## Example Entries

```markdown
## 2026-02-19

### 14:32 — Code style
- **Correction:** "Use 2-space indentation, not 4"
- **Context:** Editing TypeScript file
- **Count:** 1 (first occurrence)

### 16:15 — Communication
- **Correction:** "Don't start responses with 'Great question!'"
- **Context:** Chat response
- **Count:** 3 → **PROMOTED to memory.md**

## 2026-02-18

### 09:00 — Project: website
- **Correction:** "For this project, always use Tailwind"
- **Context:** CSS discussion
- **Action:** Added to projects/website.md
```

## 2026-03-30

### 09:40 — Security / GitHub Token
- **Correction:** "收到 GitHub Token 后没有立即写入 MEMORY，导致之后找不到"
- **Context:** 用户说之前发过 Token，但我没存，无法回答
- **Count:** 1
- **Action:** 已写入 MEMORY.md；制定新规则：收到任何 Token/Key/密码 → 立即写入 MEMORY.md

### 09:40 — GitHub Secret Scanning
- **Correction:** "把 GitHub Token 明文写进 MEMORY.md 后 commit，被 GitHub 拦截"
- **Context:** push 时 GH013 错误，PUSH PROTECTION 阻止
- **Count:** 1
- **Action:** 已 reset commit；制定铁律：Token 不进任何文件，敏感信息只存环境变量

### 09:40 — Gateway Restart
- **Correction:** "exec 里调 gateway restart 会把 exec 进程 kill 掉，导致断 session"
- **Context:** 多次尝试重启 Gateway 都会导致跳转登录页
- **Count:** 1
- **Action:** 创建 `scripts/gateway-watchdog.ps1`；制定铁律：绝不调用 `openclaw gateway restart`，用 watchdog 代替

### 09:40 — Skill 质量判断
- **Correction:** "直接安装 awesome-copilot 的 gh-cli/git-commit，没验证就相信安装成功"
- **Context:** 两个 skill 都缺 SKILL.md，安装后 skills 目录里没有对应文件夹
- **Count:** 1
- **Action:** 以后用 `npx skills add` 后立即 `ls skills/` 验证是否真的存在

---

## Log Format

Each entry includes:
- **Timestamp** — When the correction happened
- **Correction** — What the user said
- **Context** — What triggered it
- **Count** — How many times (for promotion tracking)
- **Action** — Where it was stored (if promoted)
