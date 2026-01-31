class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-x for x in nums]
        heapq.heapify(h)

        for _ in range(k):
            res = heapq.heappop(h)

        return -res