class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        res = float("inf")

        for right, val in enumerate(nums):
            sum += val
            while sum >= target:
                res = min(res, right - left + 1)
                sum -= nums[left]
                left += 1
        
        if res == float("inf"):
            return 0
        else:
            return res