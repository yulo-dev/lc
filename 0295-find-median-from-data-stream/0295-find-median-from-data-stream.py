class MedianFinder:

    def __init__(self):
        # max_heap 存左半部 (存負數來模擬 max heap)
        self.small = [] 
        # min_heap 存右半部
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. 永遠先丟進左邊 (max_heap)
        heapq.heappush(self.small, -num)
        
        # 2. 把左邊最強的踢給右邊 (min_heap)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # 3. 如果右邊太重了，踢回給左邊
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            # 如果是奇數，左邊那個頂端就是中位數
            return float(-self.small[0])
        else:
            # 如果是偶數，取兩邊堆頂的平均
            return (-self.small[0] + self.large[0]) / 2.0



#適用heap的原因：
#1.資料是 streaming 進來的：每次 addNum 後都可能要立刻查 median
#2.median 其實只關心中間附近：你不需要整個排序好的序列，只需要「中間左邊最大」和「中間右邊最小」

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()