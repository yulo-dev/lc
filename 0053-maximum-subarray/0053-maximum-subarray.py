class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #模板一
        best = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            best = max(best, curr)

        return best

        #模板二
        #best = float("-inf")
        #curr = 0

        #for x in nums:
        #    if curr < 0:
        #        curr = 0
        #    curr += x
        #    best = max(best, curr)

        #return best