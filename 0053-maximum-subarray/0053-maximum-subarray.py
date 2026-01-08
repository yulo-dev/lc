class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prefix = 0
        min_prefix = 0 
        best = nums[0]

        for x in nums:
            prefix += x
            best = max(best, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)
        
        return best
                