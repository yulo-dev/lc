class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        left = 0
        right = 0
        window = 0 
        res = float("inf")

        while right < len(nums):
            window += nums[right]
            while window >= target:
                res = min(res, right - left + 1)
                window -= nums[left]
                left += 1

            right += 1

        return res if res != float("inf") else 0
