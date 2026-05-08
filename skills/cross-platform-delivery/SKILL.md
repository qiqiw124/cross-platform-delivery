---
name: cross-platform-delivery
description: 跨前端、后端、客户端通用的需求交付技能。用于用户提供设计稿、需求文档、接口文档、埋点口径或业务规则并希望快速完成跨端对齐、联调、实现规划、spec维护、代码审查和验收清单时触发。适用于新功能、复杂重构、联调排障、字段口径不一致、状态机梳理、埋点补齐等场景。
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
- 统一的是“交付产物和口径”，不是代码目录本身。
- 默认要求至少标明：
- `frontend_repo`
- `backend_repo`
- `client_repo`
- 若只有其中两端参与，本 skill 也照常可用，但要明确缺失端和影响范围。

## Workflow
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

4. 输出交付方案。
- 必须包含：改动范围、仓库归属、复用策略、数据流/状态流、接口映射、联调方案、回归范围、风险与回滚方案。
- 如果是排障或 review 场景，也要补“根因假设 + 最小验证路径”。

5. 按小步推进实现或联调。
- 建议顺序：`骨架/协议 -> 数据映射 -> 状态与容错 -> 埋点与联调 -> 回归与CR`。
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
- 始终可追踪：结论尽量附文件路径、接口名、字段名、页面名。
- 始终做映射表：跨端需求默认输出字段/状态/埋点映射。
- 始终做归属表：多仓库需求默认输出“字段归属 + 仓库归属 + 验收归属”。
- 始终维护 spec：有业务变更就更新。
- 始终做联调视角 review：不只看代码是否能跑。
- 若仓库或子模块已有更具体的本地 skill / spec / 目录规范，优先沿用本地规则，再用本 skill 做总控。
- 命中 `references/anti-patterns.md` 里的反模式时，先明确指出风险，再决定是否继续推进。

## Output Template
1. 输入门禁结果
2. 复用检索结果
3. 跨端映射表
4. 仓库归属表
5. 交付方案
6. 分步推进结果
7. spec维护结果
8. 代码审查结果
9. 验收清单

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
- `examples/maintenance.md`：shared spec / repo spec 更新场景示例
- `examples/`：真实请求场景示例
