import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.cnt = 0

    def addNum(self, num: int) -> None:
        self.cnt += 1

        heapq.heappush(self.max_heap, -num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)

        if self.min_heap and self.max_heap and -self.max_heap[0] > self.min_heap[0]:
            val_min = heapq.heappop(self.min_heap)
            val_max = heapq.heappop(self.max_heap)

            heapq.heappush(self.min_heap, -val_max)
            heapq.heappush(self.max_heap, -val_min)

    def findMedian(self) -> float:
        val_min = self.min_heap[0] if self.min_heap else 0
        val_max = -self.max_heap[0] if self.max_heap else 0

        return (val_min + val_max) / 2 if self.cnt % 2 == 0 else float(val_max)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()