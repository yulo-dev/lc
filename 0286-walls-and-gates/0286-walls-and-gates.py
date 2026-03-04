class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows = len(rooms)
        cols = len(rooms[0])
        
        queue = deque([])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))

        self.bfs(rooms, queue, visited)

    def bfs(self, rooms, queue, visited):
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in DIRECTIONS:
                new_x = dir_x + x
                new_y = dir_y + y
                if not self.is_valid(rooms, new_x, new_y, visited):
                    continue
                rooms[new_x][new_y] = rooms[x][y] + 1
                queue.append([new_x, new_y])
                visited.add((new_x, new_y))

    def is_valid(self, rooms, x, y, visited):
        rows = len(rooms)
        cols = len(rooms[0])

        if not (0 <= x < rows and 0 <= y < cols):
            return False

        if (x,y) in visited:
            return False

        return rooms[x][y] == 2147483647