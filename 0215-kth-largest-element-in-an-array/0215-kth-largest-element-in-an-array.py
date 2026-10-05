class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

        while len(heap) > k:
            heappop(heap)

        return heap[0]