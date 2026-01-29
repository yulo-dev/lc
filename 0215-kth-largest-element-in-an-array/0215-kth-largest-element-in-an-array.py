class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap) 
        
        for _ in range(k):
            val = -heapq.heappop(max_heap)
        return val