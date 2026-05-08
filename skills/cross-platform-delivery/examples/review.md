# Example: Review

## Input
- 代码变更：新增营销弹窗展示逻辑
- 关心点：字段映射、页面生命周期、前后台切换、埋点

## Expected Output Shape
1. Findings first
2. 字段/状态是否错位
3. 生命周期/幂等/前后台风险
4. 埋点缺口
5. memory或测试缺口

## Key Review Points
- 旧批次是否会误删新批次数据
- 页面重进后是否还能展示
- 前后台恢复后是否会漏拉数据
