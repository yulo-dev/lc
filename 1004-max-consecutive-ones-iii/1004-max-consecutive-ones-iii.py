class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0

        window_0 = k
        window_sum = 0
        res = 0

        while right < len(nums):
            if nums[right] == 0:
                window_0 -= 1
            window_sum += 1

            while window_0 < 0:
                if nums[left] == 0:
                    window_0 += 1
                window_sum -= 1
                left += 1

            res = max(res, window_sum)
            right += 1
        
        return res 