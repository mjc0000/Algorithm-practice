class MinStack:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self,val: int)-> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) ->None:
        popped=self.stack.pop()
        if popped ==self.min_stack[-1]:
            self.min_stack.pop()

    def top(self)->int :
        return self.stack[-1]

    def getMin(self)->int :
        return self.min_stack[-1]


'''
`typing` 库中的 `List` 与 Python 内置的 `list` 主要是在用途和使用场景上存在差异，下面为你详细阐述它们之间的关系：

### 发展历程
- 在 Python 3.5 引入类型提示（Type Hints）特性时，标准库中还没有原生支持带类型参数的泛型表示，因此 `typing` 模块应运而生，提供了 `List`、`Dict`、`Tuple` 等泛型类型用于类型注解。
- 从 Python 3.9 开始，Python 语言本身开始支持内置类型（如 `list`、`dict`、`tuple` 等）作为泛型类型使用，从而减少了对 `typing` 模块中对应类型的依赖。

### 相同点
- **本质关联**：二者本质上都和 Python 中的列表数据结构相关。无论是 `typing` 库中的 `List` 还是内置的 `list`，最终指向的都是 Python 里用于存储有序元素集合的列表类型。

### 不同点

#### 用途差异
- **`typing.List`**：它主要用于类型提示，目的是在代码里为变量、函数参数、函数返回值等指定类型，让代码的意图更加清晰，同时也有助于静态类型检查工具（如 `mypy`）对代码进行类型检查。例如：
```python
from typing import List

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

```
在这个例子中，`List[int]` 表明 `numbers` 参数应该是一个元素为整数的列表，这只是一种提示，不会影响代码的实际运行。
- **内置 `list`**：是 Python 内置的可变序列数据类型，用于在程序运行时创建和操作列表对象。例如：
```python
my_list = list([1, 2, 3])
my_list.append(4)
print(my_list)

```
这里使用 `list` 来创建和操作一个实际的列表对象。

#### 语法和使用版本差异
- **`typing.List`**：在 Python 3.9 之前是进行列表类型提示的标准方式，使用时需要从 `typing` 模块导入。例如：
```python
from typing import List

def process_items(items: List[str]):
    for item in items:
        print(item)

```
- **内置 `list`**：从 Python 3.9 开始，可以直接用于类型提示，无需导入额外的模块。例如：
```python
def process_items(items: list[str]):
    for item in items:
        print(item)

```

### 兼容性和建议
- **兼容性**：为了保证代码在旧版本 Python 中的兼容性，如果你需要支持 Python 3.9 之前的版本，仍然需要使用 `typing.List` 进行类型提示。
- **建议**：如果你的代码仅运行在 Python 3.9 及更高版本上，建议直接使用内置的 `list` 进行类型提示，这样可以减少对 `typing` 模块的依赖，使代码更加简洁。 '''