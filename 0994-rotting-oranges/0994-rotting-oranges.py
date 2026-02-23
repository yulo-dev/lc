from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        fresh = 0
        queue = deque([])
        visited = set()
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh += 1
                elif grid[x][y] == 2:
                    queue.append((x,y))
                    visited.add((x,y))
        
        fresh, minutes = self.bfs(grid, queue, visited, fresh)
        return minutes if fresh == 0 else -1

    def bfs(self, grid, queue, visited, fresh):
        DIRECTION = [(1,0), (0,1), (-1,0), (0,-1)]
        minutes = 0

        while queue and fresh > 0:
            # 【最小優化核心】：這分鐘「一開始」有多少爛橘子，就只處理那些
            # 新產生的爛橘子會被加到 queue 尾端，留到「下一分鐘」再處理
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dir_x, dir_y in DIRECTION:
                    new_x = dir_x + x
                    new_y = dir_y + y

                    if not self.is_valid(grid, new_x, new_y, visited):
                        continue

                    fresh -= 1
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
            minutes += 1
            
        return fresh, minutes

    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])

        if not (0 <= x < m and 0 <= y < n):
            return False
        if (x,y) in visited:
            return False

        return grid[x][y] == 1