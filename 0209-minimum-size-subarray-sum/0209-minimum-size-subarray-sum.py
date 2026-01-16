class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = float("inf")

        for right, val in enumerate(nums):
            total += val
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        
        if res == float("inf"):
            return 0
        else:
            return res