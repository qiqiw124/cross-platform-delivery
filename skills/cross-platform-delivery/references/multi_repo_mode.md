# Multi Repo Mode

## Suggested Input Format

```text
frontend_repo: /path/to/frontend
backend_repo: /path/to/backend
client_repo: /path/to/client

design: figma link or page
requirement: doc link or summary
api: api doc link
tracking: tracking spec
```

## Parallel Execution Guidance

- 推荐先由总控串行完成输入门禁、共享字段框架和冲突识别。
- 进入实现或验证阶段后，可按 `frontend_repo`、`backend_repo`、`client_repo` 三个分支并行推进。
- 并行分支适合处理：
- 各仓库代码检索与复用点盘点
- 各仓库实现细节与局部风险
- 各仓库回归范围与验证结果
- 不适合并行独立裁决的内容：
- 统一字段定义
- 统一状态机口径
- 统一埋点来源
- shared spec 最终内容
- 建议在并行分支结束后，统一回到总控输出一份共享映射表和仓库归属表。

## Ownership Table

| Item | Frontend Repo | Backend Repo | Client Repo | Notes |
| --- | --- | --- | --- | --- |
| Title rendering | owner | - | owner | Shared field |
| Activity API | - | owner | - | Source of truth |
| Tracking trigger | owner | - | owner | Trigger timing must match |
| Empty fallback | owner | owner | owner | Must align |

## Shared Spec
推荐单独维护一份 shared spec，记录：
- 统一业务背景
- 统一字段定义
- 状态机口径
- 埋点来源
- 联调规则
- 验收标准

## Repo Spec
每个仓库自己的 spec 记录：
- 实现文件路径
- 生命周期或框架限制
- 本地缓存/线程/状态处理
- 仓库内回归范围
