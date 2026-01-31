class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(h, (-dist, x, y))
            if len(h) > k:
                heapq.heappop(h)

        return [[x,y] for (_,x,y) in h]
