class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot_exist = 0

        for i in range(len(nums)-2, -1, -1):

            #find pivot
            if nums[i] < nums[i+1]:
                left = i
                right = len(nums) - 1

                #find the rightmost element that is > pivot
                while left < right:
                    if nums[right] > nums[left]:
                        change = right
                        break
                    right -= 1

                nums[left], nums[change] = nums[change], nums[left]

                start = left + 1
                end = len(nums) - 1

                pivot_exist = 1
                break
            
        #edge case: if no pivot, reverse the whole list
        if pivot_exist == 0:
            start = 0
            end = len(nums) - 1

        #reverse suffix
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1