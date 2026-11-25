# pairwise-bus-latency-compensate

## 领域

游戏、图形与多媒体

## 主题

混音总线延迟补偿

## 说明

延迟表统一收集、发送轨补偿、导出重算。

初始状态下 `av/bus_latency.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
