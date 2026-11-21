class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        left = 0
        right = len(nums) - 1

        res = [0] * len(nums)
        pos = len(nums) -1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] * nums[left]
                left += 1
            else:
                res[pos] = nums[right] * nums[right]
                right -= 1

            pos -= 1

        return res