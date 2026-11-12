class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        #input & output
        # input: 2D grid of integers
        # output: integer, minimum of minutes

        #clarification
        # only 0,1,2 in the grid? yes
        # is it possible to have all cell = 2? yes
        # Do all rotten oranges spread the rot to their adjacent fresh oranges simultaneously every minute? yes
        # Can there be multiple initially rotten oranges? yes
        # Should I return -1 if some fresh oranges are unreachable? yes

        #egde cases
        # can not rotten all orange -> -1
        # [[1,1][1,1]] -> -1
        # [[0]] -> 0
        # [[2]] -> 0

        # Approach:
        # 1. Treat the grid as a graph and use multi-source BFS.
        # 2. Scan the grid to add all initially rotten oranges
        #    to the queue and count the fresh oranges.
        # 3. Process the queue level by level.
        # 4. For each rotten orange, check its four neighbors.
        # 5. If a neighbor is fresh, mark it as rotten,
        #    add it to the queue, and decrease the fresh count.
        # 6. Each BFS level represents one minute of spreading.
        # 7. Return the total minutes if no fresh oranges remain;
        #    otherwise, return -1.

        if not grid:
            return 0

        queue = deque([])
        visited = set()
        fresh = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    queue.append([x,y, 0])
                    visited.add((x,y))
                elif grid[x][y] == 1:
                    fresh += 1

        if fresh == 0:
            return 0


        DIRECTIONS = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue:
            x, y, minute = queue.popleft()
            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y

                if (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])) and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    queue.append([new_x, new_y, minute + 1])
                    visited.add((new_x, new_y))
                    fresh -=1
                if fresh == 0:
                    return minute + 1

        return -1


