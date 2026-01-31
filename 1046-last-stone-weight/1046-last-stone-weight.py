class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h) > 1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)
            diff = a - b
            if diff != 0:
                heapq.heappush(h, -diff)

        return -h[0] if len(h) == 1 else 0
        