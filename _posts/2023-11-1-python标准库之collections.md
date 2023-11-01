---
title: python标准库之collections
categories: python
tags:
- python
---

tutorial for collections lib

`collections`是Python标准库中的一个模块，提供了一些额外的数据类型，这些数据类型在某些场景下比内置数据类型更加高效或方便。以下是`collections`模块提供的一些常用类型：

1. `namedtuple`: 具名元组，可以为元组的每个位置指定一个名称，使得元组的每个位置有了意义，也可以通过名称访问元组的每个位置。

2. `deque`: 双向队列，可以在队列的头部和尾部进行操作，支持高效的插入和删除。

3. `Counter`: 计数器，统计可迭代对象中元素出现的次数。

4. `OrderedDict`: 有序字典，可以记录元素插入的顺序。

5. `defaultdict`: 默认字典，可以指定字典在访问不存在的键时返回的默认值。

6. `ChainMap`: 链接字典，可以将多个字典链接为一个字典，依次查找键对应的值。

# Explain
`namedtuple`是collections模块提供的一个工厂函数，用于创建具名元组（named tuple）。具名元组是一个类似于元组的数据结构，它的每个位置都有一个名称，可以通过名称来访问元素，而不仅仅通过索引。

使用namedtuple函数创建具名元组的语法如下：


from collections import namedtuple

# 创建具名元组类
TypeName = namedtuple('TypeName', ['field1', 'field2', ...])

# 创建具名元组对象
obj = TypeName(value1, value2, ...)
其中，TypeName是具名元组的类名，['field1', 'field2', ...]是字段的列表，每个字段对应一个位置。在创建具名元组对象时，需要按照字段的顺序传入相应的值。

# deque
`deque`（双向队列）是`collections`模块中提供的一种数据类型，它是一个具有队列和栈的特性的可变序列。

与列表（list）相比，`deque`在**某些操作上具有更高的性能**，尤其是在头部插入和删除元素时。这是由于`deque`的内部实现采用了双向链表，使得在头部和尾部进行插入和删除操作的时间复杂度为O(1)。  

Q：why doese the deque have the better performance than list  

A：链表结构：deque内部使用了双向链表的数据结构，而list则是使用基于数组的线性表。链表结构使得在头部和尾部进行插入和删除操作的时间复杂度为O(1)，而list在头部插入和删除元素时，需要将其他元素进行移动，时间复杂度为O(n)。

内存分配优化：deque通过维护一个块状数组（block array）来存储数据，每个块包含多个元素。这种设计可以减少内存分配的开销，提高内存利用率。

缓存友好性：由于deque的数据存储在连续的块中，这种布局更加适合CPU缓存的访问模式。相比之下，list的元素存储在不同的位置，对于大型list的遍历或随机访问可能会导致缓存未命中，性能较差。 

下面是一些使用`deque`的常见操作：

1. 创建`deque`对象：
```python
from collections import deque

# 创建空的deque
d = deque()

# 从可迭代对象创建deque
d = deque(iterable)
```

2. 添加和删除元素：

- 在队尾添加元素：
```python
d.append(element)
```

- 在队头添加元素：
```python
d.appendleft(element)
```

- 删除并返回队尾的元素：
```python
d.pop()
```

- 删除并返回队头的元素：
```python
d.popleft()
```

3. 访问元素：

- 获取队尾的元素，但不删除：
```python
d[-1]
```

- 获取队头的元素，但不删除：
```python
d[0]
```

- 获取指定位置的元素：
```python
d[index]
```

4. 队列大小和判空：

- 获取队列的长度：
```python
len(d)
```

- 判断队列是否为空：
```python
if not d:
    # 队列为空
```

5. 旋转和反转队列：

- 旋转队列，将右侧的元素移到左侧：
```python
d.rotate(n)
```

- 反转队列中的元素：
```python
d.reverse()
```

`deque`提供了一种灵活且高效的数据结构，适用于需要频繁在队列的两端进行插入和删除操作的场景。它还提供了其他一些方法，如索引查找、计数等，可以根据需要选择合适的操作来操作队列中的元素。
