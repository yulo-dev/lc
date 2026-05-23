from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        queue = deque([])
        visited = set()
        island = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x,y) not in visited:
                    queue.append((x,y))
                    visited.add((x, y))
                    self.bfs(grid, queue, visited)
                    island += 1

        return island

        
    def bfs(self, grid, queue, visited):
        DIRECTIONS = [(1,0), (0,1), (0,-1), (-1,0)]

        while queue:
            x, y = queue.popleft()

            for x_dir, y_dir in DIRECTIONS:
                new_x = x + x_dir
                new_y = y + y_dir

                if self.is_valid(new_x, new_y, grid, queue, visited):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))


    def is_valid(self, x, y, grid, queue, visited):

        if (x,y) in visited:
            return False
        if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            return False

        return grid[x][y] == "1"
            
