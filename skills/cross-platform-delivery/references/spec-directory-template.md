# Spec Directory Template

适用于状态机复杂、跨端口径多、生命周期规则多、需要长期维护的需求。

```text
spec/
  overview.md
  rules.md
  tracking.md
  acceptance.md
```

## overview.md
- 背景
- 范围
- 入口
- Source of Truth
- 关键数据结构

## rules.md
- 展示规则
- 交互规则
- 去重规则
- 幂等规则
- 状态机
- 异常与降级

## tracking.md
- 事件清单
- 触发时机
- 字段来源
- 不上报条件

## acceptance.md
- 覆盖范围
- 风险点
- 最小回归路径
- 联调 case

## 何时使用目录模式
- 三端共享规则较多
- 状态机超过简单页面级描述
- 埋点规则和展示规则都较复杂
- 预计后续会持续迭代
