class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for p in points:
            x, y = p[0], p[1]
            dist = x*x + y*y
            heapq.heappush(h, (-dist, p))

            if len(h) > k:
                heapq.heappop(h)

        return [p for _, p in h] 
        
        