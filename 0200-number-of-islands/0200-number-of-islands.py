from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        visited = set()
        queue = deque([])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    queue.append((r,c))
                    visited.add((r,c))
                    self.bfs(grid,queue,visited)
                    island += 1
        
        return island
                

    def bfs(self, grid, queue, visited):
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y

                if self.is_valid(grid, new_x, new_y, queue, visited):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

    def is_valid(self, grid, x, y, queue, visited):
        if (x,y) in visited:
            return False
        if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            return False

        return grid[x][y] == "1"