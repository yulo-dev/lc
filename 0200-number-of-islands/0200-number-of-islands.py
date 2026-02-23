from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        visited = set()
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    self.bfs(i, j, grid, visited)
                    islands += 1

        return islands

    def bfs(self, x, y, grid, visited):
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque([(x,y)])
        visited.add((x,y))

        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in DIRECTIONS:
                new_x = dir_x + x
                new_y = dir_y + y

                if not self.is_valid(new_x, new_y, grid, visited):
                    continue

                queue.append((new_x, new_y))
                visited.add((new_x, new_y))


    def is_valid(self, x, y, grid, visited):
        m = len(grid)
        n = len(grid[0])

        if not (0 <= x < m and 0 <= y < n):
            return False

        if (x,y) in visited:
            return False

        return grid[x][y] == "1"
            
