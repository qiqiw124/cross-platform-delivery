# Example: Multi Repo

## Input
```text
frontend_repo: /work/web-member
backend_repo: /work/member-service
client_repo: /work/atourlife-ios

design: figma link
requirement: 业务页面新增营销弹窗入口
api: /activity/popup/config
tracking: 曝光、点击、关闭
```

## Expected Output Shape
1. 输入门禁结果
2. 复用检索结果
3. 跨端映射表
4. 仓库归属表
5. 交付方案
6. shared spec / repo spec 建议
7. 联调方案
8. 验收清单

## Sample Ownership Table
| Item | Frontend Repo | Backend Repo | Client Repo | Notes |
| --- | --- | --- | --- | --- |
| 弹窗标题展示 | owner | - | owner | 同字段，两端展示 |
| 弹窗配置接口 | - | owner | - | 后端字段源头 |
| 关闭埋点触发 | owner | - | owner | 触发时机要一致 |
| 空值兜底 | owner | owner | owner | 三端必须统一 |

## Key Review Points
- shared spec 是否已经沉淀统一字段定义
- repo spec 是否补了各端实现细节
- ownership 是否明确到“谁改、谁验、谁兜底”
- 真接口和 mock 联调路径是否都存在
