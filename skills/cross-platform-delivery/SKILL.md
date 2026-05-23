---
name: cross-platform-delivery
description: >
  Use when coordinating frontend, backend, mobile, mini-program delivery — API contracts,
  field mapping, tracking (埋点), state machines, joint debugging (联调), acceptance checklists,
  multi-repo planning, multi-platform alignment, full-stack coordination, monorepo
  (iOS + Android + web + backend, mobile + backend sync, 三端/前后端/客户端+服务端).
  Triggers on 跨端对齐/联调/设计稿/接口文档/埋点口径/字段映射/验收清单.
  Also auto-triggers when working directory or sibling dirs contain multiple platform targets
  (e.g., iOS + Android + web + backend detected in same workspace),
  when Hermes memory holds multi-platform project records,
  or when ~/.hermes/active-plan points to a cross-platform spec directory.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [cross-platform, delivery, api, alignment, debugging, acceptance, multi-repo]
    related_skills: [openspec-delivery, planning-with-files]
---

# Cross Platform Delivery

## Overview
统一前端、后端、客户端的需求交付流程：先检查输入、再读真实代码和契约；先对齐 spec、再推进实现；始终输出可联调、可审查、可回归的标准产物。

## When to Use
- 需求同时涉及前端、后端、客户端中的两端及以上。
- 需要统一字段口径、状态机、埋点规则、验收清单。
- 需要在多仓库之间做联调排障、交付收口或 review。
- 需要先做跨端映射，再进入某一端的实现。

## When Not to Use
- 问题只发生在单一仓库，且不涉及跨端口径时，不必先走总控，可直接进入端内 skill 或直接改代码。
- 用户只需要某个局部函数、某个页面、某个接口的小改动，且上下游契约稳定时，不必强制拉起完整跨端流程。
- 已经有明确 spec、字段映射和验收口径，只需要纯实现时，可把本 skill 作为补充而不是入口。

## Auto-Detection — Proactive Multi-Platform Discovery

本 skill 应在每次会话启动、切换工作目录或面对新仓库时**主动自检**是否适用。不需要等用户指明"跨端"，先扫后报。

### 检测范围
- 优先扫 `cwd`（当前工作目录）
- 若 `cwd` 只含单端，扩展扫同级目录（`../` 下的一级子目录）
- **Memory 感知**：检索 Hermes memory 中是否记录过多平台项目（如「YouWozai 项目有 iOS + Android + uniCloud 三端」）。若有，视为跨端场景，自动触发本 skill。
- **Active-plan 感知**：读取 `~/.hermes/active-plan`，若指向的 spec 目录包含多仓库归属或跨端映射表，自动触发。

### 平台信号（满足任一即视为检测到对应端）

| 端 | 强信号（高置信） | 弱信号（辅助确认） |
| --- | --- | --- |
| iOS | `*.xcodeproj`, `*.xcworkspace`, `Podfile`, `Package.swift` | 大量 `.swift`/`.m` 文件 + UIKit/SwiftUI import |
| Android | `build.gradle` / `build.gradle.kts` + `AndroidManifest.xml` | `settings.gradle`, `gradlew`, `*.kt` + Jetpack Compose import |
| 前端 (Web) | `package.json` + (`react`/`vue`/`next`/`nuxt` 在 dependencies 中) | `vite.config.*`, `next.config.*`, `tsconfig.json`, `src/` + `.tsx`/`.vue` |
| 后端 | `package.json` + (`express`/`koa`/`fastify`/`nestjs` 在 dependencies), `go.mod` + 服务端框架, `requirements.txt` + `flask`/`fastapi`/`django`, `pom.xml` + Spring | `src/` + 路由/controller/model 目录, Dockerfile, `docker-compose.yml` |
| 小程序 | `app.json` + `project.config.json`（微信）, `app.acss`（支付宝） | `miniprogram/` 目录, `uni.scss`（uni-app） |
| 跨端框架 | `capacitor.config.*`, `ionic.config.json`, `app.json` + `taro`/`uni-app` 依赖 | `flutter`/`react-native` 在 package.json |

### 检测后动作
1. 输出检测摘要：检测到哪些端，信号来源（具体文件路径）。
2. 若 ≥2 端：**自动进入本 skill 总控流程**，先输出各端仓库路径和已有 spec/memory 状态，不等待用户确认。
3. 若仅 1 端：不激活本 skill，但仍可在用户后续提到跨端需求时手工触发。
4. 检测结果写入短期上下文（不污染 memory），仅本次会话有效。

### 检测粒度原则
- 宁可多报也不少漏。误报成本低（用户一句话否定），漏报成本高（整套跨端流程被跳过）。
- 弱信号达到 2 个以上，且至少一个强信号时，视为确认。
- 仅弱信号：提示用户「疑似多端结构，是否确认？」。

## Preconditions
- 先读真实代码、类型定义、接口 schema、测试，再读 spec。
- 设计稿、需求说明、接口文档、埋点要求至少要拿到核心部分；缺失时先列缺失项和影响范围。
- code / schema / spec 冲突时，先指出冲突点，不直接实现。
- 不把历史总结、口头约定或旧文档当作裁决依据。

## Expected Input
- 参与仓库：`frontend_repo`、`backend_repo`、`client_repo`，至少给出本次相关的仓库路径。
- 需求摘要：功能目标、问题现象，或 review 范围。
- 契约输入：接口文档、schema、类型定义、示例数据，至少给出一种。
- 埋点输入：事件名、触发时机、字段来源；没有时明确说明缺失。
- 当前任务类型：新功能、联调排障、收口 review、重构迁移。

## If Input Is Missing
- 先列出缺失项和影响范围。
- 能继续的部分先继续，例如先做代码检索、相似模块复用检索、现状梳理。
- 不能继续的部分明确卡点，不直接猜字段、状态、契约或埋点规则。

## Source Priority
- 实现行为以真实代码、类型定义、接口 schema、测试为准。
- 规则口径以当前 spec 为准。
- 若 code / schema / spec 冲突，先指出冲突点，不直接猜测。
- 不再依赖历史总结作为裁决依据。

## Quick Decisions
- 只涉及单一仓库且不影响跨端契约：不必先走总控。
- 跨两端及以上，或字段/状态/埋点要统一：先走本 skill。
- 规则简单、一次性需求：默认 `spec.md`。
- 状态机复杂、埋点复杂、长期维护：升级到 `spec/` 目录模式。
- 已有明确 spec 且只差实现：把本 skill 作为补充，不强制重走全流程。

## Routing Guide
| Scenario | Default Path | Must Read | Then Do | Output Focus |
| --- | --- | --- | --- | --- |
| 新功能交付 | flat spec | `references/quickstart.md`, `references/mapping_template.md` | 先做输入门禁和映射表，再补交付方案 | 映射表、交付方案、验收清单 |
| 联调排障 | flat spec | `references/delivery_checklist.md`, `references/scenario-matrix.md` | 先按层排查输入、接口、状态、生命周期 | 分层排查、最小验证路径 |
| 多仓库协作 | flat spec | `references/multi_repo_mode.md` | 先拆仓库归属，再补 shared/repo spec | 仓库归属、shared/repo spec |
| 复杂状态机/复杂埋点 | `spec/` 目录模式 | `references/spec-directory-template.md` | 先拆 overview、rules、tracking、acceptance | overview、rules、tracking、acceptance |
| 收口 review | flat spec | `references/delivery_checklist.md`, `references/scenario-matrix.md` | findings first，再补 spec/测试缺口 | findings、风险、spec/测试缺口 |

## Multi-Repo Mode
- 当三端分别位于不同仓库时，仍然使用本 skill 做总控。
- 统一的是"交付产物和口径"，不是代码目录本身。
- 默认要求至少标明：
- `frontend_repo`
- `backend_repo`
- `client_repo`
- 若只有其中两端参与，本 skill 也照常可用，但要明确缺失端和影响范围。

## Spec Directory Convention

所有跨端交付产物（spec、映射表、验收清单、handoff）统一存放，不与项目代码混合。

| 产物 | 位置约定 | 示例 |
| --- | --- | --- |
| shared spec / flat spec.md | `<spec_root>/<project>/<requirement>/`（未配置时回退到项目 `.spec/`） | `/Users/wangqiqi/Desktop/sproject/.spec/sos-alert/` |
| 映射表 mapping.md | 同上目录 | `<spec_root>/<project>/<requirement>/mapping.md` |
| 验收清单 acceptance.md | 同上目录 | `<spec_root>/<project>/<requirement>/acceptance.md` |
| 仓库归属表 ownership.md | 同上目录 | `<spec_root>/<project>/<requirement>/ownership.md` |
| handoff.md | 同上目录 | `<spec_root>/<project>/<requirement>/handoff.md` |
| repo spec（各端） | `<spec_root>/<project>/<requirement>/<platform>/` | `<spec_root>/youwozai/sos-alert/ios/` |
| 复杂 spec/ 目录模式 | `<spec_root>/<project>/<requirement>/spec/` | `spec/overview.md`, `spec/rules.md`, `spec/tracking.md`, `spec/acceptance.md` |

**spec_root 确定规则：**
1. 若 `~/.hermes/active-plan` 文件存在且指向一个有效目录 → 以该目录为 spec_root。
2. 若 memory 中记录了用户的 spec 目录偏好（如「spec 文件放在 `/Users/wangqiqi/Desktop/spec-history/`」）→ 以该路径为 spec_root。
3. 若以上都不存在 → 回退到项目根目录下：以各端仓库的共同父目录或 cwd 作为锚点，在其中创建 `.spec/<requirement>/` 作为 spec_root。例如多端项目都放在 `/Users/wangqiqi/Desktop/sproject/` 下，则 spec_root = `/Users/wangqiqi/Desktop/sproject/.spec/<requirement>/`。
4. 若连项目目录都无法确定（如零散仓库无共同父目录）→ 询问用户指定 spec_root，并写入 memory。
5. spec_root 一旦确定，本轮所有产物都写入该目录下；中途不切换。

**active-plan 管理：**
- `~/.hermes/active-plan` 是一个纯文本文件，内容为当前活跃的 spec 目录绝对路径。
- 开始新需求时，写入该路径；需求关闭后，清空文件内容。
- 下次会话启动时，Auto-Detection 读取此文件判断是否有活跃的跨端上下文。

## Task Model
- 默认执行模型是"串行总控 + 并行分支 + 串行收口"。
- 串行总控阶段必须先完成：输入门禁、复用检索、冲突识别、映射框架搭建。
- 当任务天然可拆成互不阻塞的仓库切片、角色切片或验证切片时，应并行推进。
- 并行分支只负责本分支的事实收集、实现细节、局部风险和验证结果，不单独裁决跨端口径。
- 所有并行分支最终必须回到总控收口，统一输出映射表、仓库归属、风险、spec 和验收清单。
- 如果下一步直接依赖上一步产物，例如接口字段尚未统一、状态机冲突未解决、埋点口径未定，则必须回到串行推进。

### When to Use delegate_task (Parallel Workers)
| 场景 | 拆分粒度 | worker 职责 | 禁止事项 |
| --- | --- | --- | --- |
| 代码检索 | 按仓库拆：`ios_worker` / `android_worker` / `backend_worker` | 各自独立检索本端代码、模型、接口、埋点，返回"候选复用清单" | 不允许 worker 擅自改文件或裁决跨端冲突 |
| 联调排障 | 按检查主题拆：`api_check` / `state_check` / `lifecycle_check` / `tracking_check` | 各自只核对本层事实（接口响应、状态流转、生命周期日志、埋点落点），返回"误差清单" | 不允许 worker 判定根因或给出修改方案 |
| 收口 review | 按检查主题拆：`field_mapping` / `state_machine` / `lifecycle` / `tracking` / `test_gap` | 各自只列出 findings，返回"风险清单" | 不允许 worker 自行修复或补充测试 |
| 多仓库 spec 起草 | 按仓库拆：各自起草本端的 `repo spec` | 只写本端约束，引用 shared spec 中的字段定义 | 不允许独自修改 shared spec 中的口径 |

### When NOT to Use delegate_task
- 输入门禁阶段（事实基础不统一，拆开必定冲突）
- 跨端映射表的最终裁决（必须总控一人拍板）
- 工作目录中只有一个仓库（无并行收益）
- worker 结果之间有强依赖（先串行对齐，再考虑并行）

### delegate_task 使用规则
- 使用 Hermes 的 `delegate_task` 工具，`role='leaf'`。
- 每个 worker 的 `context` 必须包含：仓库绝对路径、当前已知的字段/接口契约、禁止事项。
- worker 返回后，总控必须逐一验证关键结果（如文件路径是否存在），不能盲信。
- 并行 worker 数量默认 ≤3，对应 `delegation.max_concurrent_children` 默认值。

## Workflow
0. 自动检测多端环境。
- 按 Auto-Detection 章节执行文件扫描 + memory 检索 + active-plan 读取。
- 输出检测结果：发现哪些端、哪些仓库、当前 spec/memory 状态。
- 若 ≥2 端：继续 Step 1。
- 若仅 1 端但用户明确说有跨端需求：继续 Step 1。

1. 执行输入门禁。
- 至少确认：设计稿或交互稿、需求说明、接口文档、埋点要求、页面/接口入口。
- 多仓库模式下，额外确认三端仓库路径、主分支、改动归属和联调环境。
- 缺少关键输入时，先输出“缺失项清单 + 影响范围”，不要直接猜字段、状态或交互。

2. 优先检索真实实现与现有 spec。
- 默认先看相似模块代码、类型定义、接口模型、测试、已有埋点实现、`spec.md`、`docs/spec/`。
- 输出“候选复用点清单”：文件、模块、接口、状态机、埋点、缓存策略。

3. 做跨端对齐。
- 拆出三类信息：前端展示与交互、后端接口与时序、客户端状态与生命周期。
- 输出字段/状态/埋点映射表：设计语义、接口字段、端内字段、埋点字段、空值兜底、异常兜底、兼容策略。
- 若发现冲突，先列冲突点和建议，不直接进入实现。

### 冲突裁决协议 (Conflicts Resolution Protocol)

当字段名、状态流转、接口契约在多端之间存在不一致时，按以下优先级裁决：

| 优先级 | 裁决来源 | 适用场景 | 说明 |
| --- | --- | --- | --- |
| 1 | **后端接口 schema** | 接口字段名、请求/响应结构、错误码、枚举值 | 后端是数据的唯一权威源，字段名以后端为准；前端和客户端映射为端内字段 |
| 2 | **PRD / 产品规格文档** | 状态流转规则、页面跳转逻辑、交互行为 | 产品文档定义的业务规则优先于任意端的实现惯例 |
| 3 | **已有线上行为** | 现网已生效的接口、字段、状态 | 向后兼容优先；要改的话必须评估影响面并列入风险 |
| 4 | **埋点规范** | 事件名、字段名、上报时机 | 埋点团队定义的规范优先，一端自创字段需升级为共享口径 |

裁决流程：
1. 列出冲突项 → 标注冲突来源（哪端不同、差异是什么）
2. 按优先级表给出建议方案 → 附理由
3. 若优先级相同的两个来源冲突（如后端有两套接口都声称权威）→ 标记为 **ESCALATE**，提请用户决策
4. 已裁决的冲突写入映射表的「冲突-已解决」列；ESCALATE 项写入「冲突-待决策」列
5. 待决策项不计入映射表定稿条件，但必须出现在 Exit Conditions 的未闭合风险中

禁止行为：
- 禁止以「某一端先实现了」为由直接采纳为该端的实现方式
- 禁止绕过裁决协议直接硬编码字段名或状态值
- 禁止在 ESCALATE 项未解决时声称映射表已定稿

4. 输出交付方案。
- 必须包含：改动范围、仓库归属、复用策略、数据流/状态流、接口映射、联调方案、回归范围、风险与回滚方案。
- 如果是排障或 review 场景，也要补“根因假设 + 最小验证路径”。

5. 按小步推进实现或联调。
- 建议顺序：`骨架/协议 -> 数据映射 -> 状态与容错 -> 埋点与联调 -> 回归与CR`。
- 若仓库边界清晰，可在“骨架/协议”之后并行拆分 `frontend/backend/client` 三个分支推进。
- 若任务是排障，可并行拆“接口响应核对 / 前端状态核对 / 客户端生命周期核对 / 埋点日志核对”这些独立验证分支。
- 若任务是 review，可并行拆“字段映射 / 状态机 / 生命周期 / 埋点 / 测试缺口”这些检查分支。
- 每一步都输出：当前改动、验证方式、剩余风险。
- 需要快速起草交付物时，可运行 `scripts/init_delivery_artifacts.py --name <feature-name>` 生成默认轻量模板：`mapping.md`、`spec.md`、`acceptance.md`、`ownership.md`。
- 若需求复杂，可运行 `scripts/init_delivery_artifacts.py --name <feature-name> --spec-mode dir` 生成 `spec/` 目录模板。

6. 强制维护业务 spec。
- 只要涉及业务规则、状态机、缓存、埋点、页面生命周期、前后台行为，就更新对应 spec。
- 多仓库模式下，优先拆成两层：
- `shared spec`：三端共用的业务口径、字段定义、埋点来源、验收规则。
- `repo spec`：各端自己的实现约束、生命周期、框架限制、代码路径。
- 可直接参考 `references/shared-spec-template.md` 起草 shared spec。
- 若没有现成 spec，新增业务 spec 文件并补充索引。

7. 执行代码审查。
- 除非用户明确跳过，完成后默认做 review。
- 优先检查：字段错位、状态不一致、埋点缺失、生命周期回归、幂等问题、弱网/前后台切换、测试缺口。

8. 输出验收清单。
- 默认给出三端都能执行的联调/提测清单：已覆盖项、未覆盖风险、最小回归路径、关键异常 case。
- 多仓库模式下，额外输出“仓库维度验收归属”，标明每一项由哪一端验证。

## Invocation Patterns
- 面向前端：用于对齐页面状态、交互稿、文案、埋点口径和接口依赖。
- 面向后端：用于梳理字段口径、时序、幂等、错误码、兼容策略和联调 case。
- 面向客户端：用于对齐模型映射、页面生命周期、本地状态、前后台行为和埋点落点。
- 面向三端协作：用于统一需求口径、排查联调问题、维护 spec 和输出验收清单。
- 面向多仓库全栈：用于统一三个项目的字段口径、改动归属、shared spec 和跨仓库联调清单。

## Execution Rules
- 始终先对齐：需求、接口、埋点未对齐时，不直接编码。
- 始终先读真实实现：先找代码、模型、接口、组件、状态机、测试，再看 spec。
- 默认先串行建立总控上下文，再决定是否拆并行 task。
- 只有在分支之间写入范围清晰、事实来源独立、不会互相阻塞时才并行。
- 并行 task 必须按“仓库归属”或“检查主题”拆分，避免多个分支同时改同一份事实口径。
- 并行 task 的结果必须由总控统一归并，不允许各分支各自输出最终结论。
- 始终可追踪：结论尽量附文件路径、接口名、字段名、页面名。
- 始终做映射表：跨端需求默认输出字段/状态/埋点映射。
- 始终做归属表：多仓库需求默认输出“字段归属 + 仓库归属 + 验收归属”。
- 始终维护 spec：有业务变更就更新。
- 始终做联调视角 review：不只看代码是否能跑。
- 若仓库或子模块已有更具体的本地 skill / spec / 目录规范，优先沿用本地规则，再用本 skill 做总控。
- 命中 `references/anti-patterns.md` 里的反模式时，先明确指出风险，再决定是否继续推进。

## Output Template
0. 自动检测结果（多端发现摘要）
1. 输入门禁结果
2. 复用检索结果
3. 跨端映射表
4. 仓库归属表
5. 交付方案
6. 分步推进结果
7. spec维护结果
8. 代码审查结果
9. 验收清单

## Exit Conditions — Handoff to Per-Platform Implementation

以下条件**全部满足**时，跨端总控阶段结束，可进入各端独立实现：

1. **映射表定稿**：字段/状态/埋点映射表已输出，所有冲突已标注建议方案且无遗留。
2. **shared spec 已落地**：`shared spec`（或 `spec.md`）文件已写入或更新，包含本次需求的完整口径。
3. **各端 repo spec 已就位**（多仓库模式）：每端有自己的 `repo spec`，明确本端约束和实现边界。
4. **验收清单已输出**：联调/提测清单已给出，每条标注归属端。
5. **本轮未闭合风险已明确**：若有未解决的冲突、缺失输入、或需要跨端联调才能验证的点，已在清单中标注为 pending。
6. **用户确认**：总控向用户展示以上 5 项摘要，获得确认后，退出总控模式。

退出后，各端进入自己的实现阶段。总控保留义务：联调阶段重新介入，按验收清单做收口 review。

### Handoff Artifact — Cross-Session Continuity

每次退出总控模式时，必须写入交接文件 `handoff.md` 到当前 spec 目录下，内容：

```markdown
# Handoff — 跨端总控交接

- 日期：YYYY-MM-DD
- 项目/需求：
- 参与的端及仓库路径：
- 映射表位置：
- shared spec 位置：
- 各端 repo spec 位置：
- 已解决冲突（摘要）：
- 待决策冲突（ESCALATE）：
- 本轮未闭合风险：
- 验收清单位置：
- 下一步动作（哪个端先开始、联调什么时候要介入）：
```

下次会话自动检测到 spec 目录中存在 `handoff.md` 时，优先读取而非从零开始。

### Re-Entry — 联调阶段自动介入

总控退出后，以下信号触发总控重入：

| 触发信号 | 检测方式 | 动作 |
| --- | --- | --- |
| 用户明确请求联调或收口 | 用户说"联调"/"收口"/"全量review" | 读取 handoff.md + 验收清单，进入收口 review 路径 |
| 多端实现完成 | 用户说"各端都改完了"或"可以联调了" | 对验收清单逐项核验，输出联调通过/不通过结果 |
| spec 目录中 pending 项已解决 | 用户手动更新了 handoff.md 或 spec | 重新检查 Exit Conditions，确认后可正式关闭本轮 |
| 新一轮需求触发 | 新功能需求涉及原有映射表 | 走 Routing Guide 中的"新功能交付"路径，以现有 spec 为基线增量推进 |

重入时不重新做 Auto-Detection（仓库结构通常不变），直接读取已有 spec 和 handoff.md 恢复上下文。

## Common Pitfalls

1. **跳过自动检测直接编码**：看到一个问题就开始改代码，没先扫工作目录是否有其他端受影响。应始终先做 Auto-Detection。
2. **输入不足时猜字段**：设计稿/接口文档/埋点要求任一缺失时，直接假设字段名或状态逻辑。应先列缺失项和影响范围，能继续的先继续，不能继续的明确卡点。
3. **把历史总结当裁决依据**：依赖旧 memory、口头约定或过时文档做字段口径裁决，而不是读当前真实代码和 schema。
4. **并行 worker 越权**：worker 自作主张修改 shared spec 或裁决跨端冲突。worker 只能收集事实和列出 findings，所有裁决必须由总控统一完成。
5. **盲信 worker 自述结果**：worker 说"文件已写入"就认为完成，不验证路径是否真实存在。关键产物（spec 文件、映射表）必须总控自行确认。
6. **spec 更新滞后**：代码改完了才想起来更新 spec，或者改了 spec 但忘了同步到各端 repo spec。应每完成一个阶段就立即更新对应 spec。
7. **shared spec 和 repo spec 混淆**：把端内实现细节（如某个 Swift 类的初始化方式）写到 shared spec 里，或者把跨端口径（如埋点字段名）只写在一个 repo spec 里。
8. **验收清单偏向一端**：只从前端视角写验收 case，忽略了客户端生命周期、后台行为、弱网切换等维度。验收清单必须覆盖参与的所有端。
9. **Greenfield 项目用错模板**：新建项目无代码可检索时，仍走"先检索真实实现"流程。应直接参考 `references/greenfield-scaffolding.md`，按 PRD + API 契约推进。
10. **退出条件不满足就开始实现**：映射表还有冲突未解决，就进入各端编码。必须先达成退出条件，再做实现。

## Verification Checklist

- [ ] Auto-Detection 已执行，检测结果已输出摘要（哪些端、哪些仓库）。
- [ ] 输入门禁已通过：设计稿/需求文档/接口文档/埋点要求至少拿到核心部分，缺失项已列明。
- [ ] 真实代码/类型定义/接口 schema/测试已检索，候选复用点清单已输出。
- [ ] 字段/状态/埋点映射表已定稿，冲突点已标注建议方案。
- [ ] 仓库归属表已输出（多仓库模式）。
- [ ] 交付方案已包含：改动范围、数据流/状态流、联调方案、回归范围、风险与回滚方案。
- [ ] shared spec 已写入或更新。
- [ ] 各端 repo spec 已写入或更新（多仓库模式）。
- [ ] 代码审查已完成（或用户明确跳过）。
- [ ] 验收清单已输出，每条标注归属端和验证方式。
- [ ] Exit Conditions 全部满足，用户已确认退出总控。

## References
- `references/quickstart.md`：最常用的简短提问模板
- `references/delivery_checklist.md`：输入、联调、回归与 review 清单
- `references/mapping_template.md`：字段/状态/埋点映射表示例
- `references/role-entrypoints.md`：按前端/后端/客户端/三端协作划分的入口问法与输出重点
- `references/scenario-matrix.md`：按新功能、联调排障、review、重构分类的建议流程
- `references/multi_repo_mode.md`：多仓库输入格式、仓库归属表、shared spec 建议
- `references/anti-patterns.md`：常见跨端协作反模式与纠偏方式
- `references/shared-spec-template.md`：多仓库共享业务 spec 模板
- `references/repo-spec-template.md`：单仓库实现 spec 模板
- `references/spec-directory-template.md`：复杂需求使用的 `spec/` 目录模板
- `references/maintenance.md`：shared spec / repo spec 维护建议
- `references/greenfield-scaffolding.md`：全新多端项目脚手架搭建流程（用于无可检索代码的 Greenfield 场景）
- `examples/maintenance.md`：shared spec / repo spec 更新场景示例
- `examples/`：真实请求场景示例
