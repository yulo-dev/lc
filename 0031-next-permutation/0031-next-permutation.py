class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #find peak
        #find the smallest number that is bigger than peak
        #switch
        #reverse the suffix nums

        pivot_exist = 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                left = i
                right = len(nums) - 1

                while left < right:
                    if nums[right] > nums[left]:
                        switch = right
                        break
                    right -= 1

                nums[left], nums[switch] = nums[switch], nums[left]

                start = left + 1
                end = len(nums) - 1

                pivot_exist = 1
                break

        if pivot_exist == 0:
            start = 0
            end = len(nums) - 1

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
