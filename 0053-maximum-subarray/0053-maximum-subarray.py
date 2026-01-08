class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        prefix = 0
        min_profit = 0 
        best = nums[0]

        for x in nums:
            prefix += x
            best = max(best, prefix - min_profit)
            min_profit = min(min_profit, prefix)
        
        return best
                