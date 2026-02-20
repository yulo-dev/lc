class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        # 1. 先把所有數字變成 heap (O(N))
        self.h = nums
        heapq.heapify(self.h)
        
        # 2. 既然我們要的是「第 K 大」，那我們只需要維持 Heap 的大小為 K
        # 多的就踢掉 (大的踢掉剩下的就是前 K 大，因為是 Min-Heap)
        # 這步可做可不做
        while len(self.h) > k:
            heapq.heappop(self.h)
      
    def add(self, val: int) -> int:
        heapq.heappush(self.h, val) # O(log K)

        if len(self.h) > self.k:
            heapq.heappop(self.h) # O(log K)

        return self.h[0]
     

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)