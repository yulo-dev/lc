class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []  # store (-dist, x, y)

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(h, (-dist, x, y))
            if len(h) > k:
                heapq.heappop(h) # pop farthest among kept k

        return [[x,y] for (_, x, y) in h]