from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque([])
        visited = set()
        fresh = 0
        minutes = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    visited.add((x,y))
                    queue.append((x,y,minutes))
                elif grid[x][y] == 1:
                    fresh += 1
        
        fresh, minutes = self.bfs(grid, queue, visited, fresh)

        if fresh == 0:
            return minutes
        else:
            return -1

    def bfs(self, grid, queue, visited, fresh):

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        minutes = 0

        while queue:
            x, y, minutes = queue.popleft()
            for dir_x, dir_y in directions:
                new_x = x + dir_x
                new_y = y + dir_y

                if self.is_valid(grid, new_x, new_y, visited):
                    queue.append((new_x, new_y, minutes+1))
                    visited.add((new_x, new_y))
                    fresh -= 1

        return fresh, minutes

    def is_valid(self, grid, x, y, visited):

        if (x, y) in visited:
            return False
        if not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            return False

        return grid[x][y] == 1
