class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        cumsum = 0

        for n in nums:
            if cumsum < 0:
                cumsum = 0

            cumsum += n
            res = max(res, cumsum)

        return res

        