class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {}
        prefix[0] = 1
        curr_sum = 0
        res = 0

        for n in nums:
            curr_sum += n

            if curr_sum - k in prefix:
                res += prefix[curr_sum - k]

            if curr_sum not in prefix:
                prefix[curr_sum] = 1
            else:
             prefix[curr_sum] += 1

            

        return res
