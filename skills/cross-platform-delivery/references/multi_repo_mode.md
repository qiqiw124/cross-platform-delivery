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

## Ownership Table

| Item | Frontend Repo | Backend Repo | Client Repo | Notes |
| --- | --- | --- | --- | --- |
| Title rendering | owner | - | owner | Shared field |
| Activity API | - | owner | - | Source of truth |
| Tracking trigger | owner | - | owner | Trigger timing must match |
| Empty fallback | owner | owner | owner | Must align |

## Shared Memory
推荐单独维护一份 shared memory，记录：
- 统一业务背景
- 统一字段定义
- 状态机口径
- 埋点来源
- 联调规则
- 验收标准

## Repo Memory
每个仓库自己的 memory 记录：
- 实现文件路径
- 生命周期或框架限制
- 本地缓存/线程/状态处理
- 仓库内回归范围
