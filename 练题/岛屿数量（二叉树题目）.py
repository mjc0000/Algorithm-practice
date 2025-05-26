'''
要计算二维网格中岛屿的数量，可采用深度优先搜索（DFS）或者广度优先搜索（BFS）的方法。
这里选用深度优先搜索的方法，其核心思路是：一旦发现一块陆地（值为 '1'），
就将与之相连的所有陆地都标记为已访问（可将其置为 '0'），同时岛屿数量加 1。
'''

from typing import  List



class Solution:
    def numIsland(self,grid:List[list[str]]) ->int:
        def dfs(i,j):
            if i<0 or i>=len(grid) or  j<0 or j>=len(grid[0]) or grid[i][j] != '1':
                return #但下面还要继续
            grid[i][j]='0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        count =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count+=1

        return count