class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sorted, remove duplicate, in place: fast slow pointer

        write = 0

        for read in range(len(nums)):
            if write == 0 or nums[read] != nums[write-1]:

                #read 提供值，write 決定放哪
                nums[write] = nums[read]
                write += 1

        return write