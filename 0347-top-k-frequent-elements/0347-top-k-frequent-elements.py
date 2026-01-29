class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = Counter(nums)

        h = []

        for num, freq in cnt.items():
            heapq.heappush(h, (freq, num))
            if len(h) > k:
                heapq.heappop(h)

        return [num for (_, num) in h]
