class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #if I XOR all numbers together, all the duplicates cancel out, 
        #and only the unique number remains.
        res = 0
        for num in nums:
            res ^= num
        return res