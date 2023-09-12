
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.dfs(grid)
            
    def dfs(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRS = [(0,1), (0,-1), (1,0), (-1,0)]

        def nav(row, col): 
            if not(0 <= row < m) or not(0 <= col < n) or grid[row][col] == '0':
               return 

            grid[row][col] = '0'

            for dr, dc in DIRS:
                nav(row+dr, col+dc)

        icount = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1': 
                    nav(r, c)
                    icount += 1
                    # self.printgrid(r, c, grid)
        return icount

    def bfs(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
        m, n = len(grid), len(grid[0])
        queue = []
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1': 
                    queue.append((r, c))
                    
                    while queue:
                        pr, pc = queue.pop()                    
                        neighbors = [(pr+dr, pc+dc) for dr, dc in DIRECTIONS
                                        if  0 <= (row := pr+dr) < m and 
                                            0 <= (col := pc+dc) < n and 
                                            grid[row][col] == '1']
                        queue.extend(neighbors)   
                        grid[pr][pc] = '0'   
                    count += 1
        return count          

    def printgrid(self, row, col, grid):
        print(f"{row=} {col=} {grid[row][col]=}")
        for r in range(len(grid)):
            print(''.join([grid[r][c] for c in range(len(grid[0]))]))


