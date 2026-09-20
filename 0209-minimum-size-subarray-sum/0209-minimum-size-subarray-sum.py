class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        res = float("inf")
        window = 0

        for i in range(len(nums)):
            right = i
            window += nums[right]

            while window >= target:

                if window >= target:
                    res = min(res, right - left + 1)
                
                window -= nums[left]
                left += 1
                

        return res if res != float("inf") else 0