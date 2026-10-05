class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        freq = {}
        heap = []

        for n in nums:
            freq[n]= freq.get(n,0) + 1

        for key,val in freq.items():
            heapq.heappush(heap, (val,key))

            while len(heap) > k:
                heapq.heappop(heap)

        return [n for _, n in heap]

        
        