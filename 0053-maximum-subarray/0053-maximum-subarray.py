class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's Algorithm

        curr = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i]) # restart or extend
            best = max(best, curr)

        return best