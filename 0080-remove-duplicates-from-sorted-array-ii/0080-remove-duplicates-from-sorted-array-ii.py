class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #keyword: sorting, remove dup, in place: fast-slow pointers
        
        write = 0
        for read in range(len(nums)):
            if write < 2 or (write >= 2 and nums[read] != nums[write-2]):
                nums[write] = nums[read]
                write += 1

        return write
