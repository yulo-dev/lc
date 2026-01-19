class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        visited = set()

        #Flood Fill 只需要從 (sr, sc) 的連通區域開始擴散，不是把所有 orig_color 的點都 fill
        self.bfs(image, sr, sc, visited, color, orig_color)

        return image

    def bfs(self, image, x, y, visited, color, orig_color):
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque([(x,y)])
        visited.add((x,y))

        while queue:
            x, y = queue.popleft()
            image[x][y] = color #出 queue 就染一次
            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y
                if not self.is_valid(image, new_x, new_y, visited, orig_color):
                    continue
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
    
    def is_valid(self, image, x, y, visited, orig_color):
        m = len(image)
        n = len(image[0])

        if not (0 <= x < m and 0 <= y < n):
            return False
        if (x,y) in visited:
            return False
        return image[x][y] == orig_color
