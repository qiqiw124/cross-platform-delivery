# Example: Maintenance

## Input
- 需求已上线，但埋点口径变了
- 后端接口字段新增了一个兼容开关
- 客户端页面生命周期有调整

## Expected Output Shape
1. 哪些内容要进 shared memory
2. 哪些内容只进 repo memory
3. 哪些内容要同步更新验收清单
4. 哪些内容会影响三端联调

## Rule of Thumb
- 改变业务口径、字段定义、埋点来源、状态机，优先更新 shared memory
- 只改变某个仓库的实现细节、路径、生命周期处理，更新 repo memory
- 如果本地实现变化会反向影响三端口径，shared memory 和 repo memory 都要更新

## Key Review Points
- shared memory 是否描述了“以后大家都按这个口径理解”
- repo memory 是否描述了“这个仓库里具体怎么做”
- 验收清单是否同步了新的异常 case
