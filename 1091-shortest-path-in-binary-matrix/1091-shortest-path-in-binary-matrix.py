class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 特殊情況：起點或終點被堵住
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1
        
        queue = deque([(0,0)])
        length = self.bfs(grid, queue)
        return length

    def bfs(self, grid, queue):
        m = len(grid)
        n = len(grid[0])

        # 初始化 visited 並加入起點座標
        visited = {(0, 0)}

        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
        length = 1

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # --- 核心停損點: 抵達終點，立刻回傳步數 ---
                if x == m - 1 and y == n - 1:
                    return length

                for dir_x, dir_y in DIRECTIONS:
                    new_x = x + dir_x
                    new_y = y + dir_y
                    if not self.is_valid(grid, new_x, new_y, visited):
                        continue

                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

            length += 1
        return -1 # 如果走不到終點，回傳 -1

    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])

        if not (0 <= x < m and 0 <= y < n):
            return False

        if (x,y) in visited:
            return False

        return grid[x][y] == 0