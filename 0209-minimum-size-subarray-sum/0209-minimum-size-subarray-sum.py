class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left  = 0
        window = 0 
        res = float("inf")

        for i in range(len(nums)):
            right = i
            window += nums[right]

            while window >= target:
                res = min(res, right - left + 1)
                window -= nums[left]
                left += 1
                
        return res if res != float("inf") else 0