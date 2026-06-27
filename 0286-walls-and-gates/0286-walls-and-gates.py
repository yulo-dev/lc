class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        # shortest path
        queue = deque() # expand from these position
        visited = set() # visited grid

        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        self.bfs(rooms, queue, visited)


    def bfs(self, rooms, queue, visited):
        DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y

                if self.is_valid(rooms, new_x, new_y, visited):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
                    rooms[new_x][new_y] = rooms[x][y] + 1

    def is_valid(self, rooms, x, y, visited):
        rows = len(rooms)
        cols = len(rooms[0])

        if (x,y) in visited or not (0 <= x < rows and 0 <= y < cols):
            return False
        
        return rooms[x][y] == 2147483647