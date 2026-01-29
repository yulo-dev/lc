class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h) > 1:
            y = -heapq.heappop(h)  # largest
            x = -heapq.heappop(h)  # second largest

            if y != x:
                heapq.heappush(h, -(y - x))
        
        return -h[0] if h else 0
