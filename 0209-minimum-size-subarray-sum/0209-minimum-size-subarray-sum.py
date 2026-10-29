class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        left = 0
        right = 0
        tot = 0

        res = float("inf")

        while right < len(nums):
            
            tot += nums[right]
            right += 1

            while tot >= target:

                res = min(res, right - left)

                tot -= nums[left]
                left += 1

        return res if res != float("inf") else 0
                