from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        visited = set()
        island = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) not in visited and grid[x][y] == "1":
                    self.bfs(grid, x, y, visited)
                    island += 1
        return island

    def bfs(self, grid, x, y, visited):
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque([(x,y)])
        visited.add((x,y))

        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in DIRECTIONS:
                new_x = dir_x + x
                new_y = dir_y + y
                if not self.is_valid(grid, new_x, new_y, visited):
                    continue
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
        
    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])

        if (x, y) in visited:
            return False
        if not (0 <= x < m) or not (0 <= y < n):
            return False

        return grid[x][y] == "1"