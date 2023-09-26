
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.using_bfs(grid)

    def using_dfs(self, grid): 
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        islands = 0 

        def dfs(r, c):
            if 0 <= r < M and 0 <= c < N and (r, c) not in visited and grid[r][c] == "1":
                visited.add((r, c))
                for dr, dc in DIRECTIONS:
                    dfs(r+dr, c+dc)        

        for row in range(M):
            for col in range(N):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1

        return islands
    
    def using_bfs(self, grid):
        M, N = len(grid), len(grid[0])
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        queue = []
        islands = 0

        for row in range(M):
            for col in range(N):
                if grid[row][col] == "1" and (row, col) not in visited:   
                    queue.append((row, col)) # this is the starting point and to do later   

                    while queue:
                        nr, nc = queue.pop()

                        neighbors = [(nr+dr, nc+dc) for dr, dc in DIRECTIONS
                                            if 0 <= nr+dr < M and 
                                               0 <= nc+dc < N and 
                                               grid[nr+dr][nc+dc] == "1" and 
                                               (nr+dr, nc+dc) not in visited]
                        queue.extend(neighbors)                        

                        visited.add((nr, nc)) # this is taken care of 

                    islands += 1

        return islands

