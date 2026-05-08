# Mapping Template

优先输出一张跨端映射表，再进入实现或联调。

| 设计语义 | 前端字段/状态 | 后端字段 | 客户端字段 | 埋点字段 | 空值兜底 | 异常兜底 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 标题 | `title` | `title` | `viewModel.title` | - | `""` | 隐藏标题区 | 文案来自后端 |
| 按钮可用态 | `enabled` | `status` | `isEnabled` | `button_status` | `false` | 禁用点击 | 客户端二次映射 |
| 活动ID | - | `marketId` | `model.marketId` | `activity_id` | `""` | 不上报事件 | 埋点口径取后端 |

若存在冲突，先输出：
- 冲突点
- 影响范围
- 建议统一口径
- 临时兼容方案
