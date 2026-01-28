class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return None

        m = len(mat)
        n = len(mat[0])
        res = [[0] * n for _ in range(m)]

        queue = deque()
        visited = set()

        for x in range(m):
            for y in range(n):
                if mat[x][y] == 0:
                    queue.append((x,y,0))
                    visited.add((x,y))
                    res[x][y] = 0
        
        res = self.bfs(mat, queue, visited, res)
        return res

    def bfs(self, mat, queue, visited, res):
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            x, y, dist = queue.popleft()
            for dir_x, dir_y in DIRECTIONS:
                new_x = dir_x + x
                new_y = dir_y + y

                if not self.is_valid(mat, new_x, new_y, visited):
                    continue
                
                res[new_x][new_y] = dist + 1
                queue.append((new_x, new_y, dist + 1))
                visited.add((new_x, new_y))

        return res

    def is_valid(self, mat, x, y, visited):
        m = len(mat)
        n = len(mat[0])

        if not (0 <= x < m and 0 <= y < n):
            return False

        if (x,y) in visited:
            return False

        return mat[x][y] == 1

