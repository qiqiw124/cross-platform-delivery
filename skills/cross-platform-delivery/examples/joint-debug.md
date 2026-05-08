# Example: Joint Debug

## Input
- 现象：客户端按钮不可点击，但前端 H5 页面可点击
- 接口：`status=1`
- 客户端表现：按钮灰态
- 埋点：点击未上报

## Expected Output Shape
1. 复现条件
2. 三端口径对比
3. 最小根因假设
4. 最小验证路径
5. 临时兼容建议
6. 回归清单

## Key Review Points
- 字段含义是否被三端解释成不同语义
- 客户端是否有本地状态覆盖接口值
- 埋点是否被 UI 状态短路
