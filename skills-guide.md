# OpenClaw技能大全（31个技能完整指南）

> 更新时间：2026-03-27 | 技能总数：30个

---

## 一、技能总览

本指南详细介绍虾仁（你的OpenClaw AI助手）已激活的30个技能，包括它们的功能、激活方式、使用方法和效果。

| 编号 | 技能名称 | 功能描述 | 触发关键词 |
|------|----------|----------|------------|
| 1 | ask-ai | AI自动求助技能 | 帮我问下豆包、你问问AI |
| 2 | agent-browser | 浏览器自动化 | 网页自动化、填表测试 |
| 3 | auto-updater | 自动更新 | 自动后台运行 |
| 4 | automation-workflows | 自动化工作流 | 帮我自动化XXX |
| 5 | baoyu-xhs-images | 小红书图片生成 | 小红书图片、XHS |
| 6 | brainstorming | 头脑风暴 | 创建功能、头脑风暴 |
| 7 | copywriting | 文案撰写 | 写文案、营销文案 |
| 8 | feishu-doc-best-practices | 飞书文档最佳实践 | 飞书文档、权限 |
| 9 | find-skills | 技能发现 | 找一个技能 |
| 10 | gog | Google工作区 | Gmail、日历、Drive |
| 11 | grimoire-polymarket | 预测市场 | Polymarket |
| 12 | humanizer | 去AI味 | 去AI味、润色 |
| 13 | mcp-debug | MCP调试 | MCP问题 |
| 14 | multi-search-engine | 多引擎搜索 | 搜索、web search |
| 15 | ontology | 知识图谱 | 记住、link X to Y |
| 16 | planning-with-files | 文件规划 | 规划、组织任务 |
| 17 | proactive-agent | 主动Agent | 自动启用 |
| 18 | remotion-video-toolkit | 视频工具 | 视频生成 |
| 19 | self-improving | 自我进化 | 自动启用 |
| 20 | self-improving-agent | 通用自我进化 | 自动启用 |
| 21 | skill-vetter | 技能审查 | 安装前检查 |
| 22 | speech-to-text | 语音转文字 | 转录、语音转文字 |
| 23 | stock-market-pro | 股票分析 | 股票、股价 |
| 24 | summarize | 网页摘要 | 总结、摘要 |
| 25 | test-driven-development | TDD开发 | 实现功能、bugfix |
| 26 | ui-ux-pro-max | UI/UX设计 | 设计界面、UI |
| 27 | web-access | 联网操作 | 搜索、访问网站 |
| 28 | web-content-fetcher | 网页内容提取 | 抓取网页 |
| 29 | xiaohongshu-deep-research | 小红书研究 | 小红书话题研究 |
| 30 | youtube-watcher | YouTube字幕 | YouTube、字幕 |

---

## 二、每个技能详细介绍

### 1. ask-ai - AI自动求助技能

**功能描述**：当遇到难题时，自动求助豆包/千问/Kimi/DeepSeek等AI获取方案。

**触发方式**：
- 显式触发：帮我问下豆包、帮我问下千问、你问问AI
- 自动触发：这个我不会、把握程度<50%、推荐其他方案

**效果/产出**：遇到不确定的问题时自动调用AI讨论，返回经过验证的解决方案

**使用方法**：直接说"帮我问下豆包XXX"或触发自动判断

**配置路径**：.openclaw/skills/ask-ai → 已复制到 workspace/skills/ask-ai

---

### 2. agent-browser - 浏览器自动化

**功能描述**：Rust-based headless浏览器自动化CLI，支持AI代理导航、点击、输入和截图。

**触发方式**：
- 自动化网页交互
- 提取结构化数据
- 填表程序化
- 测试网页UI

**效果/产出**：自动完成网页操作、数据抓取、表单填写

**使用方法**：说"帮我自动化XXX网页操作"

**配置路径**：workspace/skills/agent-browser

---

### 3. auto-updater - 自动更新

**功能描述**：每天自动检查并更新Clawdbot和所有已安装技能。运行cron，检查更新，应用更改，并向用户发送变更摘要。

**触发方式**：通过cron每日自动运行

**效果/产出**：保持所有技能在最新版本

**使用方法**：自动后台运行，无需手动触发

**配置路径**：workspace/skills/auto-updater

---

### 4. automation-workflows - 自动化工作流

**功能描述**：设计并实现自动化工作流以节省时间和扩展运营。作为 solopreneur 使用。识别自动化机会，跨工具构建工作流，设置触发器和动作，或优化现有自动化。

**触发方式**：
- automate、automation
- workflow automation
- save time、reduce manual work
- no-code automation

**效果/产出**：识别自动化机会，设计工作流，选择工具（Zapier/Make/n8n）

**使用方法**：说"帮我自动化XXX流程"

**配置路径**：workspace/skills/automation-workflows

---

### 5. baoyu-xhs-images - 小红书图片生成

**功能描述**：生成小红书（Little Red Book）信息图系列，包含11种视觉风格和8种布局。将内容分解为1-10张针对XHS优化的小卡通风格图片。

**触发方式**：
- 小红书图片、XHS images
- RedNote infographics
- 小红书种草
- wants social media infographics for Chinese platforms

**效果/产出**：将内容拆分为1-10张卡通风格图片

**使用方法**：说"生成小红书图片"并提供内容

**配置路径**：.openclaw/skills/baoyu-xhs-images → 已复制到 workspace/skills/baoyu-xhs-images

---

### 6. brainstorming - 头脑风暴

**功能描述**：你必须在任何创意工作之前使用——创建功能、构建组件、添加功能或修改行为。探索用户意图、需求和设计，然后才能实现。

**触发方式**：
- 创建功能
- 构建组件
- 添加功能
- 修改行为

**效果/产出**：在实现前明确需求和设计方向，避免返工

**使用方法**：说"帮我头脑风暴一下XXX"

**配置路径**：workspace/skills/brainstorming

---

### 7. copywriting - 文案撰写

**功能描述**：当用户想要为任何页面编写、重写或改进营销文案时使用。包括首页、着陆页、定价页、功能页、关于页面或产品页面。

**触发方式**：
- write copy for
- improve this copy
- rewrite this page
- marketing copy
- headline help、CTA copy
- value proposition、tagline

**效果/产出**：生成吸引人的营销文案

**使用方法**：说"帮我写一段文案"并提供页面类型和内容

**配置路径**：.openclaw/skills/copywriting → 已复制到 workspace/skills/copywriting

---

### 8. feishu-doc-best-practices - 飞书文档最佳实践

**功能描述**：飞书文档创建和权限管理的最佳实践。用于：1) 创建飞书文档时避免空内容bug；2) 处理文档权限问题；3) 排查飞书API调用失败。

**触发方式**：
- 飞书文档创建
- 权限问题
- API调用失败

**效果/产出**：避免空内容bug，处理权限问题

**使用方法**：创建飞书文档时自动应用

**配置路径**：workspace/skills/feishu-doc-best-practices

---

### 9. find-skills - 技能发现

**功能描述**：帮助用户发现和安装代理技能。当用户问"如何做X"、"找一个做X的技能"、"有没有能做...的技能"时使用。

**触发方式**：
- how do I do X
- find a skill for X
- is there a skill that can...
- 表达想要扩展能力的兴趣

**效果/产出**：搜索并安装新技能

**使用方法**：说"帮我找一个做XXX的技能"

**配置路径**：workspace/skills/find-skills

---

### 10. gog - Google工作区

**功能描述**：Google Workspace CLI for Gmail, Calendar, Drive, Contacts, Sheets, and Docs.

**触发方式**：
- gmail
- calendar
- drive

**效果/产出**：管理Google日历、邮件、文件

**使用方法**：说"帮我查下Google日历"

**配置路径**：workspace/skills/gog

---

### 11. grimoire-polymarket - 预测市场

**功能描述**：查询 Polymarket 市场数据和 CLOB 状态，并通过 Grimoire venue CLI 包装器管理 CLOB 订单。

**触发方式**：
- 预测市场
- polymarket

**效果/产出**：获取预测市场数据

**使用方法**：说"查看XXX的预测市场"

**配置路径**：.openclaw/skills/grimoire-polymarket → 已复制到 workspace/skills/grimoire-polymarket

---

### 12. humanizer - 去AI味

**功能描述**：移除AI生成写作的痕迹，使文本更自然。基于Wikipedia全面的"AI写作痕迹"指南。检测和修复模式包括：膨胀的象征主义、促销语言、浅薄的-ing分析、模糊的归属、破折号过度使用、规则三、AI词汇、负面并列和过多连词短语。

**触发方式**：
- remove AI writing
- humanize
- 去AI味
- make it sound more natural

**效果/产出**：去除AI写作特征，更像人写

**使用方法**：说"帮我润色这段文字，去掉AI味"

**配置路径**：workspace/skills/humanizer

---

### 13. mcp-debug - MCP调试

**功能描述**：MCP（Model Context Protocol）服务调试和问题排查。用于：1) 检查MCP服务是否安装；2) 配置MCP服务器到OpenClaw；3) 排查MCP连接问题。

**触发方式**：
- MCP问题
- MCP连接

**效果/产出**：检查/配置/排查MCP连接问题

**使用方法**：说"帮我排查MCP问题"

**配置路径**：workspace/skills/mcp-debug

---

### 14. multi-search-engine - 多引擎搜索

**功能描述**：17个搜索引擎集成（8个中国+9个全球）。支持高级搜索运算符、时间过滤器、站点搜索、隐私引擎和 WolframAlpha 知识查询。无需API密钥。

**触发方式**：
- web search
- search
- tavily、exa

**效果/产出**：多引擎搜索，支持高级搜索符

**使用方法**：说"帮我搜索XXX"

**配置路径**：workspace/skills/multi-search-engine

---

### 15. ontology - 知识图谱

**功能描述**：结构化代理记忆和可组合技能的类型化知识图谱。用于创建/查询实体（Person、Project、Task、Event、Document）、链接相关对象、执行约束、将多步动作规划为图转换，或当技能需要共享状态时。

**触发方式**：
- remember
- what do I know about
- link X to Y
- show dependencies
- entity CRUD

**效果/产出**：创建/查询实体，链接相关对象

**使用方法**：说"记住XXX"

**配置路径**：workspace/skills/ontology

---

### 16. planning-with-files - 文件规划

**功能描述**：实现Manus风格的文件规划，追踪复杂任务进度。创建task_plan.md、findings.md和progress.md。当被要求规划、分解或组织多步骤项目、研究任务或任何需要>5个工具调用的工作时使用。

**触发方式**：
- plan out
- break down
- organize
- multi-step project
- research task

**效果/产出**：创建task_plan.md等文件追踪进度

**使用方法**：说"帮我规划一下XXX项目"

**配置路径**：workspace/skills/planning-with-files

---

### 17. proactive-agent - 主动Agent

**功能描述**：将AI代理从任务执行者转变为主动伙伴，预测需求并持续改进。现在具有WAL协议、Working Buffer、Autonomous Crons和经过验证的模式。Hal Stack的一部分。

**触发方式**：
- 主动
- proactive
- 长时间运行任务

**效果/产出**：预测需求，持续改进

**使用方法**：自动启用

**配置路径**：workspace/skills/proactive-agent

---

### 18. remotion-video-toolkit - 视频工具

**功能描述**：Remotion+React的程序化视频创建完整工具包。涵盖动画、计时、渲染（CLI/Node.js/Lambda/Cloud Run）、字幕、3D、图表、文字效果、过渡和媒体处理。

**触发方式**：
- video
- remotion

**效果/产出**：创建数据驱动的视频模板

**使用方法**：说"帮我生成视频"

**配置路径**：workspace/skills/remotion-video-toolkit

---

### 19. self-improving - 自我进化

**功能描述**：自我反思+自我批评+自我学习+自我组织记忆。代理评估自身工作，犯错并永久改进。

**触发方式**：
- 自我改进
- improve
- 每次技能执行后

**效果/产出**：从经验中持续学习和改进

**使用方法**：自动启用

**配置路径**：workspace/skills/self-improving

---

### 20. self-improving-agent - 通用自我进化

**功能描述**：从所有技能经验中学习的通用自我改进代理。使用多记忆架构（语义+情景+工作）持续进化代码库。技能完成/错误时自动触发基于hook的自我修正。

**触发方式**：
- self-improving
- 技能执行完成/出错

**效果/产出**：多记忆架构持续进化

**使用方法**：自动启用

**配置路径**：.openclaw/skills/self-improving-agent → 已复制到 workspace/skills/self-improving-agent

---

### 21. skill-vetter - 技能审查

**功能描述**：AI代理的安全优先技能审查。在从ClawdHub、GitHub或其他来源安装任何技能之前使用。检查红旗、权限范围和可疑模式。

**触发方式**：
- 审查技能
- vet skill
- 安装新技能前

**效果/产出**：检查技能安全性和权限范围

**使用方法**：安装新技能前自动检查

**配置路径**：workspace/skills/skill-vetter（两边都有）

---

### 22. speech-to-text - 语音转文字

**功能描述**：用ElevenLabs Scribe和Whisper模型转录音频。模型：ElevenLabs Scribe v2（98%+准确率，diarization）、Fast Whisper Large V3、Whisper V3 Large。功能：转录、翻译、多语言、时间戳、说话人分离、音频事件标记。

**触发方式**：
- speech to text
- transcribe
- 语音转文字
- stt
- 会议转录
- 字幕生成

**效果/产出**：会议转录、字幕生成、语音笔记

**使用方法**：说"帮我转录这段音频"

**配置路径**：.openclaw/skills/speech-to-text → 已复制到 workspace/skills/speech-to-text

---

### 23. stock-market-pro - 股票分析

**功能描述**：专业股票价格跟踪、基本面分析和财务报告工具。支持全球市场（美国、韩国等）、Crypto和Forex，实时数据。功能：1) 实时报价；2) 估值指标（PE、EPS、ROE）；3) 财报日历和共识；4) 高质量K线图和技术指标（MA5/20/60）。

**触发方式**：
- 股票
- stock
- 股价
- finance

**效果/产出**：实时报价、估值指标、财报分析

**使用方法**：说"帮我看下XXX股票"

**配置路径**：.openclaw/skills/stock-market-pro → 已复制到 workspace/skills/stock-market-pro

---

### 24. summarize - 网页摘要

**功能描述**：总结URL或文件（网页、PDF、图片、音频、YouTube）。使用summarize CLI。

**触发方式**：
- summarize
- 总结
- 摘要

**效果/产出**：提取内容摘要

**使用方法**：说"帮我总结这个链接"

**配置路径**：.openclaw/skills/summarize → 已复制到 workspace/skills/summarize

---

### 25. test-driven-development - TDD开发

**功能描述**：实现任何功能或修复bug前使用TDD。先写测试，看它失败，再写最小代码通过。核心原则：不看到测试失败就不知道是否测试了正确的东西。

**触发方式**：
- implement
- feature
- bugfix

**效果/产出**：先写测试再看失败，确保测试正确

**使用方法**：说"用TDD方式实现XXX"

**配置路径**：workspace/skills/test-driven-development

---

### 26. ui-ux-pro-max - UI/UX设计

**功能描述**：网页和移动端UI/UX设计智能。包含50+风格、161种配色、57种字体搭配、161种产品类型、99条UX指南、25种图表类型，涵盖10个技术栈（React、Next.js、Vue、Svelte、SwiftUI等）。

**触发方式**：
- design
- UI
- UX

**效果/产出**：设计页面、选择配色、优化体验

**使用方法**：说"帮我设计XXX界面"

**配置路径**：workspace/skills/ui-ux-pro-max

---

### 27. web-access - 联网操作

**功能描述**：所有联网操作必须通过此skill处理，包括：搜索、网页抓取、登录后操作、网络交互等。触发场景：用户要求搜索信息、查看网页内容、访问需要登录的网站、操作网页界面、抓取社交媒体内容（小红书、微博、推特等）、读取动态渲染页面、以及任何需要真实浏览器环境的网络任务。

**触发方式**：
- 搜索
- 网页抓取
- 登录网站

**效果/产出**：搜索信息、访问网站、操作网页

**使用方法**：说"帮我查下XXX"

**配置路径**：.openclaw/skills/web-access → 已复制到 workspace/skills/web-access

---

### 28. web-content-fetcher - 网页内容提取

**功能描述**：网页正文内容提取。支持 Jina Reader / Scrapling+html2text / web_fetch 三级降级策略，自动返回干净的 Markdown 格式正文，保留标题、链接、图片URL、列表结构。能读取微信公众号文章（Jina 做不到的场景）。

**触发方式**：
- 抓取URL
- 提取网页
- 网页内容

**效果/产出**：提取网页正文，保留结构

**使用方法**：说"抓取这个网页内容"

**配置路径**：workspace/skills/web-content-fetcher

---

### 29. xiaohongshu-deep-research - 小红书研究

**功能描述**：小红书话题深度研究。当用户想要研究话题、分析趋势、从热门帖子收集见解或生成总结报告时使用。通过搜索抓取帖子，提取高互动内容，生成带帖子链接的分析。

**触发方式**：
- 小红书研究
- XHS research

**效果/产出**：分析趋势，提取高互动内容

**使用方法**：说"研究一下小红书XXX话题"

**配置路径**：workspace/skills/xiaohongshu-deep-research

---

### 30. youtube-watcher - YouTube字幕

**功能描述**：获取YouTube视频字幕。当需要总结视频、回答关于内容的问题或从中提取信息时使用。

**触发方式**：
- youtube
- 字幕
- video
- 视频内容

**效果/产出**：提取视频内容，总结问答

**使用方法**：说"帮我看这个YouTube视频"

**配置路径**：workspace/skills/youtube-watcher

---

## 三、技能分类索引

### 🔍 信息获取类
- multi-search-engine（多引擎搜索）
- web-content-fetcher（网页内容提取）
- summarize（网页摘要）
- youtube-watcher（YouTube字幕）
- xiaohongshu-deep-research（小红书研究）
- stock-market-pro（股票分析）
- gog（Google工作区）

### 🎨 内容创作类
- copywriting（文案撰写）
- baoyu-xhs-images（小红书图片）
- ui-ux-pro-max（UI/UX设计）
- remotion-video-toolkit（视频工具）

### 🔧 开发工具类
- agent-browser（浏览器自动化）
- test-driven-development（TDD开发）
- mcp-debug（MCP调试）
- skill-vetter（技能审查）

### 🧠 AI增强类
- ask-ai（AI自动求助）
- brainstorming（头脑风暴）
- planning-with-files（文件规划）
- humanizer（去AI味）

### 🔄 自动化类
- automation-workflows（工作流自动化）
- auto-updater（自动更新）
- web-access（联网操作）

### 📡 飞书类
- feishu-doc-best-practices（飞书文档最佳实践）

### 🧬 自我进化类
- self-improving（自我进化）
- self-improving-agent（通用自我进化）
- proactive-agent（主动Agent）
- ontology（知识图谱）

### 🎯 垂直领域
- speech-to-text（语音转文字）
- grimoire-polymarket（预测市场）
- find-skills（技能发现）

---

## 四、Q&A

### Q1: 技能如何触发？

A: 大部分技能会根据你输入的关键词自动触发。例如说"帮我搜索XXX"会自动调用多引擎搜索技能，说"帮我写一段文案"会调用文案撰写技能。一些技能如自动更新、自我进化是后台自动运行的。

### Q2: 技能在哪里配置？

A: 技能文件位于 `workspace/skills/` 目录，配置信息在 `openclaw.json` 的 `skills.entries` 部分。每个技能对应一个文件夹，包含SKILL.md定义文件。

### Q3: 如何禁用不需要的技能？

A: 在openclaw.json中将对应技能的 `enabled` 改为 false。例如要把ask-ai禁用：
```json
"ask-ai": {
  "enabled": false
}
```

### Q4: 新技能如何安装？

A: 有两种方式：
1. 从ClawHub安装：`npx skills add <owner/repo>`
2. 手动复制：将技能文件夹复制到 `workspace/skills/` 目录

### Q5: 技能之间会冲突吗？

A: 不会，技能独立运行，按需触发。每个技能有自己明确的触发条件和功能范围。

### Q6: 技能文件可以自定义修改吗？

A: 可以。所有技能文件都在你的workspace目录下，你可以根据需要修改SKILL.md来调整技能的行为。

### Q7: 技能需要网络连接吗？

A: 大部分技能需要联网才能正常工作，特别是涉及搜索、网页抓取、AI对话的技能。一些本地功能如文件规划、去AI味可以在离线状态下使用。

### Q8: 技能有使用限制吗？

A: 大部分技能没有使用限制，但部分需要API密钥的技能（如股票分析需要数据源API）可能受到配额限制。

---

## 五、快速使用指南

### 常用场景对照表

| 你想做什么 | 使用的技能 | 怎么说 |
|------------|------------|--------|
| 查资料 | multi-search-engine | 帮我搜索XXX |
| 总结网页 | summarize | 帮我总结这个链接 |
| 生成图片 | baoyu-xhs-images | 生成小红书图片 |
| 写文案 | copywriting | 帮我写一段营销文案 |
| 设计界面 | ui-ux-pro-max | 帮我设计XXX界面 |
| 转录音频 | speech-to-text | 帮我转录这段音频 |
| 查股票 | stock-market-pro | 帮我看下XXX股票 |
| 去AI味 | humanizer | 帮我去掉这段话的AI味 |
| 问AI | ask-ai | 帮我问下豆包XXX |
| 头脑风暴 | brainstorming | 帮我头脑风暴一下 |

---

## 六、技能激活状态说明

### 激活状态

| 状态 | 含义 | 数量 |
|------|------|------|
| ✅ 已激活 | 在workspace/skills目录且配置enabled=true | 30 |
| ❌ 未激活 | 在.openclaw/skills但未复制或未配置 | 10+ |

### 最近激活的技能（2026-03-27）

- ask-ai（从.openclaw/skills复制）
- agent-network
- baoyu-xhs-images
- copywriting
- grimoire-polymarket
- self-improving-agent
- speech-to-text
- stock-market-pro
- web-access
- summarize

---

## 七、配置文件位置

```
C:\Users\danie\.openclaw\
├── workspace\               # 主工作区
│   └── skills\              # 已激活的技能目录
│       ├── ask-ai\
│       ├── agent-browser\
│       ├── ...
│       └── web-content-fetcher\
│
├── skills\                  # 原始技能目录（部分未激活）
│   ├── ask-ai\              # 已激活
│   ├── feishu-doc\          # 飞书内置
│   ├── prompt-guard\       # 内置
│   └── ...
│
└── openclaw.json            # 主配置文件
    └── skills.entries        # 技能启用配置
```

---

*本文档由虾仁自动生成 | 2026-03-27*