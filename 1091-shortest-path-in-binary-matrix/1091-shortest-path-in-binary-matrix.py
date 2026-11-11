class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        #use bfs
        #put the starting point in a queue
        #start bfs: traverse the eight directions
        #and if there's a pth(i.e., 0)
        #add in the queue, and add distance + 1 for each level(=each step)
        #until we meet the bottom right cell (= grid[len(grid)-1][len(grid[0])-1]

        if not grid or grid[0][0] == 1:
            return -1

        queue = deque([])
        queue.append([0,0,1])

        visited = set()
        visited.add((0,0))

        DIST = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

        while queue:
            x, y, dist = queue.popleft()
            if x == len(grid)-1 and y == len(grid[0])-1:
                return dist

            for dist_x, dist_y in DIST:
                new_x = x + dist_x
                new_y = y + dist_y

                if (0<=new_x<len(grid) and 0<=new_y<len(grid[0])) and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                    queue.append([new_x, new_y, dist + 1])
                    visited.add((new_x, new_y))

        return -1
