class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        visited = set()

        self.bfs(image, sr, sc, orig_color, color, visited)

        return image

    def bfs(self, image, sr, sc, orig_color, color, visited):
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = deque([(sr, sc)])
        visited.add((sr, sc))

        while queue:
            x, y = queue.popleft()
            image[x][y] = color
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