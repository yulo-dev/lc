class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0

        visited = set()
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = self.bfs(grid, i, j, visited)
                    max_area = max(max_area, area)

        return max_area


    def bfs(self, grid, x, y, visited):
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque([(x,y)])
        visited.add((x,y))
        area = 0

        while queue:
            x, y = queue.popleft()
            area += 1
            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y

                if not self.is_valid(grid, new_x, new_y, visited):
                    continue

                queue.append((new_x,new_y))
                visited.add((new_x,new_y))

        return area


    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])

        if not (0 <= x < m and 0 <= y < n):
            return False
        if (x,y) in visited:
            return False

        return grid[x][y] == 1