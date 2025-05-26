from typing import List
from collections import deque



class Solution:
    def orangesRotting(self,grid: List[List[int]]) ->int:
        rows =len(grid)
        cols =len(grid[0])
        rotten =deque()

        fresh_count =0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                     rotten.append((i,j))
                elif grid[i][j]==1:
                    fresh_count+= 1


        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        minutes=0
        while rotten and fresh_count>0:
            size = len(rotten)

            for _ in range(size):
                x,y=rotten.popleft()
                for dx,dy in directions:
                    new_x,new_y = x+dx,y+dy
                    if 0<=new_x < rows and 0<= new_y <cols and grid[new_x][new_y]==1:

                        grid[new_x][new_y]=2
                        rotten.append((new_x, new_y))
                        fresh_count-=1
            minutes+=1

        return minutes if fresh_count ==0 else -1

#型数据类型  元组
#deque是一个创建双端队列的函数

'''Python 标准库 `collections` 中的 `deque`（双端队列）类本身并不存在“默认”左删右增的设定。`deque` 提供了在两端进行操作的方法，如 `append()`、`appendleft()`、`popleft()`、`pop()` 等，开发者可以根据具体的算法和数据处理需求自由选择使用哪些方法。

在“橘子腐烂”问题的代码中，之所以采用从左端删除（`popleft()`）和从右端添加（`append()`）的操作方式，是为了契合广度优先搜索（BFS）算法先进先出（FIFO）的特性。

在 BFS 中，我们希望先处理最早发现的节点（在这个问题中即最早出现的腐烂橘子），`popleft()` 方法可以高效地从队列头部取出元素，满足了先入先出的顺序；而 `append()` 方法将新发现的腐烂橘子（新节点）添加到队列尾部，保证了后续按顺序处理这些新节点。

但这只是针对这个具体问题和算法的选择，在其他应用场景中，比如实现栈（后进先出，LIFO）的功能时，可能会选择使用 `append()` 和 `pop()` 方法（从右端添加和删除）；如果要实现相反顺序的处理，也可以使用 `appendleft()` 和 `pop()` 等。所以 `deque` 并没有默认的左删右增，是根据实际需求来决定使用哪些方法的。 '''

'''在当前代码里，双端队列（`deque`）起到了关键作用，特别是在实现广度优先搜索（BFS）算法时。下面详细阐述双端队列在代码中的运用及其优势。

### 1. 双端队列的初始化
在代码中，使用 `rotten = deque()` 对双端队列进行初始化，这个队列用于存放腐烂橘子的位置。

```python
rotten = deque()
```

### 2. 初始腐烂橘子位置的添加
借助两层嵌套的 `for` 循环遍历网格，一旦发现值为 `2` 的单元格（代表腐烂橘子），就把其位置 `(i, j)` 以元组的形式添加到双端队列 `rotten` 中。

```python
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 2:
            rotten.append((i, j))
```

### 3. BFS 过程中双端队列的使用
在 BFS 循环中，双端队列遵循先进先出（FIFO）原则。具体步骤如下：
- 利用 `rotten.popleft()` 从队列头部取出一个腐烂橘子的位置，将其解包赋值给 `x` 和 `y`。
- 检查该腐烂橘子四个相邻方向的单元格，若相邻单元格是新鲜橘子（值为 `1`），则把它变为腐烂橘子（值设为 `2`），并将新的腐烂橘子位置添加到队列尾部。

```python
while rotten and fresh_count > 0:
    size = len(rotten)
    for _ in range(size):
        x, y = rotten.popleft()  # 从队列头部取出最早发现的腐烂橘子
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                grid[new_x][new_y] = 2
                rotten.append((new_x, new_y))  # 将新腐烂的橘子添加到队列尾部
                fresh_count -= 1
```

### 4. 双端队列的优势
- **高效的添加和移除操作**：双端队列的 `append()` 和 `popleft()` 方法的时间复杂度均为 $O(1)$，这使得在 BFS 过程中添加和移除元素非常高效。
- **符合 BFS 的 FIFO 原则**：BFS 算法要求按层次依次扩展节点，双端队列的特性能够保证先处理先发现的节点，从而实现按层扩散的效果。

综上所述，双端队列在这个问题中是实现 BFS 算法的理想数据结构，它能高效地处理腐烂橘子的扩散过程，保证算法的时间复杂度为 $O(m \times n)$，其中 $m$ 是网格的行数，$n$ 是网格的列数。 
'''