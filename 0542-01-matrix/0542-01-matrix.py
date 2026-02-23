class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return None

        m = len(mat)
        n = len(mat[0])

        #題目問的是「每個格子距離 0 的距離（一整個矩陣）」
        #所以我們需要一個跟原本一樣大的 res 矩陣 來存這些算出來的距離
        res = [[0] * n for _ in range(m)]

        queue = deque()
        visited = set()

        for x in range(m):
            for y in range(n):
                if mat[x][y] == 0:
                    queue.append((x,y))
                    visited.add((x,y))
                    res[x][y] = 0
        
        res = self.bfs(mat, queue, visited, res)
        return res

    def bfs(self, mat, queue, visited, res):
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
        dist = 0
        while queue:
            # 【層級控制】：這一層所有的點，距離 0 的步數都是 dist 
            # 跟994相同
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dir_x, dir_y in DIRECTIONS:
                    new_x = dir_x + x
                    new_y = dir_y + y

                    if not self.is_valid(mat, new_x, new_y, visited):
                        continue
                    
                    res[new_x][new_y] = dist + 1
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

            # 這一層處理完，距離加 1
            dist += 1

        return res

    def is_valid(self, mat, x, y, visited):
        m = len(mat)
        n = len(mat[0])

        if not (0 <= x < m and 0 <= y < n):
            return False

        if (x,y) in visited:
            return False

        return mat[x][y] == 1

