class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        #self.nums = nums 這個不需要 因為nums 可以是一次性輸入，用完就丟
        self.h = []
        for x in nums:
            self.add(x)


    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)