from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        fresh = 0 
        queue = deque([])
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                val = grid[i][j]
                if val == 2:
                    queue.append((i, j, 0))
                    visited.add((i, j))
                elif val == 1:
                    fresh += 1

        minutes, fresh = self.bfs(grid, queue, fresh, visited)
        return minutes if fresh == 0 else -1

    def bfs(self, grid, queue, fresh, visited):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue:
            x, y, minute = queue.popleft()
            minutes = max(minute, minutes)
            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y
                if not self.is_valid(grid, new_x, new_y, visited):
                    continue
                fresh -= 1
                queue.append((new_x, new_y, minute + 1))
                visited.add((new_x, new_y))

        return minutes, fresh

    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])

        if not (0 <= x < m) or not (0 <= y < n):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] == 1
        
                
                    

