class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_count = Counter(nums)
        h = []

        for num, freq in nums_count.items():
            heapq.heappush(h, (freq, num))

            if len(h) > k:
                heapq.heappop(h)

        return [x for _,x in h]