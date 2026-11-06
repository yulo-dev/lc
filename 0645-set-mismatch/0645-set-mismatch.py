class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        uni_nums = set()

        dup = None

        for n in nums:
            if n in uni_nums:
                dup = n
            else:
                uni_nums.add(n)
           
        for n in range(1, len(nums)+1):
            if n not in uni_nums:
                return [dup, n]