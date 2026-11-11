class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        #bfs
        #use queue: start from entrance
        #check the up, down left, right, if there is a path, add the path in the queue
        #at the same time, dist + 1
        #if the cell is at (0,x), (x,0), (x, len(maze[0])), (len(maze), x): return dist


        queue = deque([])
        queue.append([entrance[0], entrance[1],0])

        visited = set()
        visited.add((entrance[0], entrance[1]))

        DIRECTIONS = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue:
            x, y, dist = queue.popleft()

            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y

                if (0 <= new_x < len(maze)) and (0 <= new_y < len(maze[0])) and maze[new_x][new_y] != "+" and (new_x, new_y) not in visited:
                    queue.append([new_x, new_y, dist+1])
                    visited.add((new_x, new_y))

                    if new_x == 0 or new_y == 0 or new_x == len(maze)-1 or new_y == len(maze[0])-1:
                        return dist+1

        return -1