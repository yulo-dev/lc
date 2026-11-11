class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        from collections import deque

        queue = deque()
        visited = set()
        island = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    queue.append((row,col))
                    visited.add((row, col))
                    self.bfs(grid, queue, visited, island)
                    island += 1
        
        return island

    def bfs(self, grid, queue, visited, island):

        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            x, y = queue.popleft()

            for dir_x, dir_y in DIRECTIONS:
                new_x = dir_x + x
                new_y = dir_y + y

                if (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])) and grid[new_x][new_y] == "1" and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
            