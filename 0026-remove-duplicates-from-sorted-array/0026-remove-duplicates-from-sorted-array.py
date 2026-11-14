class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        write = 0
        for read in range(len(nums)):
            if read == 0 or nums[read] != nums[read-1]:
                nums[write] = nums[read] 
                write += 1

        return write
        