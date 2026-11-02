class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq

        heap = []

        for n in nums:
            heapq.heappush(heap, n)

        while len(heap) > k:
            heapq.heappop(heap)

        return heap[0]