class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        max_dp = [float("-inf")] * len(nums) 
        min_dp = [float("-inf")] * len(nums) 
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        res = max_dp[0]

        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])

            res = max(max_dp[i],res)

        return res

    #[-2,3,-4]
    #24
