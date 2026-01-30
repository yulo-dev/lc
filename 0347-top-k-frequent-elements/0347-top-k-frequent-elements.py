class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        h = []

        for key, val in cnt.items():
            heapq.heappush(h, (val, key))
            if len(h) > k:
                heapq.heappop(h)

        return [key for (_, key) in h]
        