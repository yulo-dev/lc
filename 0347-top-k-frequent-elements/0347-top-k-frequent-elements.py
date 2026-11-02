class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        from collections import defaultdict
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        import heapq 
        heap = []

        for num, cnt in freq.items():
            heapq.heappush(heap, (cnt, num)) 

        while len(heap) > k:
            heapq.heappop(heap)

        res = []
        for i in range(k-1, -1, -1):
            cnt, num = heapq.heappop(heap)
            res.append(num)

        return res
