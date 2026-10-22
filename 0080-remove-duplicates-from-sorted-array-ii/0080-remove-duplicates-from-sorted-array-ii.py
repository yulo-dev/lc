class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        read = 0
        write = 0

        for read in range(len(nums)):
            if read <= 1:
                nums[write] = nums[read]
                write += 1

            else:
                if nums[read] != nums[write-2]:
                    nums[write] = nums[read]
                    write += 1
    

        return write

