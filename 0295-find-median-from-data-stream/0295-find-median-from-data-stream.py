class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
      
    def addNum(self, num: int) -> None:

        heapq.heappush(self.max_heap, -num)
        max_n = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_n)

        if len(self.min_heap) - len(self.max_heap) > 0:
            move_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -move_num)

    def findMedian(self) -> float:

        if len(self.min_heap) == len(self.max_heap):
            n1 = self.min_heap[0]
            n2 = -self.max_heap[0]
            return (n1+n2) / 2
        else:
            return -self.max_heap[0]


# I use two heaps: a max heap for the smaller half and a min heap for the larger half.
# addNum is O(log n) for the heap operations. 
# findMedian is O(1) since we just peek at the tops. 
# Space is O(n) for storing all elements.