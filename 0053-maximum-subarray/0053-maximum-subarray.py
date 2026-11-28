class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        dp = [float("-inf")] * len(nums)
        dp[0] = nums[0]
        res = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) #要用當前的當作subarray開始 or 延續前面的subarray
            res = max(res, dp[i])

        return res