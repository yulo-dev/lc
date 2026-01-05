class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        if not grid or not grid[0]:
            return 0

        visited = set()
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i,j) not in visited:
                    tot = self.bfs(grid, i, j, visited)
                    if tot % k == 0:
                        res += 1
    
        return res

    def bfs(self, grid, i, j, visited):
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque([(i,j)])
        visited.add((i,j))
        tot = 0

        while queue:
            x, y = queue.popleft()
            tot += grid[x][y]

            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y
                if not self.is_valid(grid, new_x, new_y, visited):
                    continue

                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
        
        return tot

    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])

        if not (0 <= x < m) or not (0 <= y < n):
            return False
        if (x,y) in visited:
            return False

        return grid[x][y] > 0
        