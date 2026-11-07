class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n+1

        for i in range(n):
            index = abs(nums[i])
            if index <= n:
                nums[index - 1] = -abs(nums[index - 1])

        for i in range(n):
            if nums[i] > 0:
                return i+1
        return n+1 