class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        
        best_effort = {(0,0): 0} #best_effort[目標座標] = 從起點到這個座標，目前找到的所有路線中，「最大單步高度差」最小的值。
        heap = [(0, 0, 0)]

        while heap:
            curr_effort, r, c = heapq.heappop(heap)
            
            if curr_effort > best_effort[(r,c)]:
                continue

            DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

            for dir_x, dir_y in DIRECTIONS:
                new_x = r + dir_x
                new_y = c + dir_y
                if 0 <= new_x < len(heights) and 0 <= new_y < len(heights[0]):
                    weight = abs(heights[new_x][new_y] - heights[r][c])
                    new_effort = max(curr_effort, weight)

                    if new_effort < best_effort.get((new_x,new_y), float("inf")):
                        best_effort[(new_x, new_y)] = new_effort
                        heapq.heappush(heap, (new_effort, new_x, new_y))

            if r == len(heights) - 1 and c == len(heights[0]) - 1:
                return best_effort[(r,c)]