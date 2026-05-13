class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        heap = []
        for num, cnt in count.items():
            heap.append((-cnt, num))

        heapq.heapify(heap)

        res = []
        for _ in range(k):
            neg_cnt, num = heapq.heappop(heap)
            res.append(num)

        return res