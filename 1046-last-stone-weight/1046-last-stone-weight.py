class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h) > 1:
            y = -heapq.heappop(h)
            x = -heapq.heappop(h)
            diff = y - x
            if diff != 0:
                heapq.heappush(h, -diff)

        return -h[0] if len(h) == 1 else 0