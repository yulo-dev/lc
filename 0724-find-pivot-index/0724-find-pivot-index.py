class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        prefix = [0] * (len(nums) + 1)

        for i in range(1,len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(len(nums)):
            left = prefix[i]
            right = prefix[len(nums)] -  prefix[i+1]

            if left == right:
                return i

        return -1