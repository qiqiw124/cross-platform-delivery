# Shared Memory Template

适用于前端、后端、客户端分属不同仓库，但需要共享统一业务口径的场景。

## 1. Background
- 需求背景
- 目标用户
- 业务目的

## 2. Scope
- 涉及端：Frontend / Backend / Client
- 涉及仓库：
- 不在本次范围内的内容：

## 3. Entry Points
- 页面入口
- 接口入口
- 消息/事件入口
- 路由或跳转链路

## 4. Source of Truth
- 哪些字段以后端为准
- 哪些文案以前端/设计为准
- 哪些状态由客户端本地派生
- 哪些埋点字段来自哪一层

## 5. Unified Field Definitions
| Business Meaning | Backend Field | Frontend Field | Client Field | Tracking Field | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 6. State Machine
- 默认态
- 加载态
- 空态
- 错误态
- 禁用态
- 重试态
- 前后台切换后的状态

## 7. Interaction Rules
- 点击规则
- 展示规则
- 去重规则
- 幂等规则
- 关闭/返回规则

## 8. Tracking Rules
- 曝光事件：
- 点击事件：
- 关闭事件：
- 字段来源：
- 不上报条件：

## 9. API and Compatibility
- 接口列表
- 关键入参
- 关键出参
- 错误码
- 兼容逻辑
- 降级逻辑

## 10. Multi-Repo Ownership
| Item | Frontend Repo | Backend Repo | Client Repo | Verification Owner | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 11. Joint Debug Checklist
- 复现条件
- 请求样例
- 响应样例
- 日志位置
- 埋点验证路径

## 12. Regression Checklist
- 标准路径
- 异常路径
- 空值/缺字段
- 弱网/重试
- 前后台切换
- 重复进入

## 13. Change Log
- YYYY-MM-DD: 变更内容 / 影响范围 / 修改人
