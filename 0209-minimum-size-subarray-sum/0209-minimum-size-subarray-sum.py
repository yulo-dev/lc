class Solution:
     def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        res = float("inf")
        tot = 0

        for right, val in enumerate(nums):
            tot += val
            while tot >= target:
                res = min(res, right - left + 1)
                tot -= nums[left]
                left += 1

        return 0 if res == float("inf") else res
                