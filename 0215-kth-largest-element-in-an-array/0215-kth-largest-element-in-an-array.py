class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        neg = []

        for n in nums:
            neg.append(-n)

        heapq.heapify(neg)

        for _ in range(k):
            res = heapq.heappop(neg)

        return -res

