class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

        increase = True
        decrease = True

        
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                increase = False

            if nums[i+1] > nums[i]:
                decrease = False

        return increase or decrease
            