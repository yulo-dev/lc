class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        freq = {}

        for n in nums:
            freq[n]= freq.get(n,0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(sorted_freq[i][0])

        return res
        
        