class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        heap = []

        for n in nums:
            heapq.heappush(heap, n * n)

        res = []
        while heap:
            val = heapq.heappop(heap)
            res.append(val)

        return res