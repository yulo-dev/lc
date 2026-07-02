class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        # collect the number of 1's in the grid, if its <= health -1: return ture
        # use bfs, start from grid[0][0] and check the 4 directions,
        # if 0: add in the queue
        # if 1 & & health > 1: add in the queue & health - 1

        #起點可能就是1 要先扣血
        start_health = health - grid[0][0]
        queue = deque([(0,0,start_health)])
        visited = {}
        visited[(0,0)] = start_health

        if not self.bfs(grid,queue,visited):
            return False

        return True

    def bfs(self,grid,queue,visited):
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            x, y, health = queue.popleft()
            #判斷到終點了嗎
            if x == len(grid)-1 and y == len(grid[0])-1 and health >= 1:
                return True
            if health < 1:
                continue #還有別條路所以可以跳過走看看
            for dir_x, dir_y in DIRECTIONS:
                new_x = x + dir_x
                new_y = y + dir_y
                if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
                    continue
                new_health = health - grid[new_x][new_y]

                if self.is_valid(grid,new_x,new_y,new_health,visited):
                    queue.append((new_x, new_y, new_health))
                    visited[(new_x, new_y)] = new_health
                    
        return False

    def is_valid(self,grid,x,y,health,visited):

        if (x,y) in visited and health <= visited[(x,y)]:
            return False

        return grid[x][y] == 0 or health >= 1