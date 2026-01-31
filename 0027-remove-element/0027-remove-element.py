class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #keyword: remove element, in-place: fast slow pointers

        write = 0 
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write