class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        
        #replace invalid values with n + 1, since we only care about numbers from 1 to n.
        sz = len(nums)

        for i in range(sz):
            if nums[i] <= 0 or nums[i] > sz:
                nums[i] = sz + 1

        #for each number x, I'll use index x - 1 as its marker and make the value at that position negative to indicate that x exists.
        for n in nums:
            index = abs(n) - 1
            if index <= sz-1:
                nums[index] = -abs(nums[index])

        #orig  0, 1, 2, 3
        #value 4, 2, 3, 1
        #index 3, 1, 2, 0


        #The first index that still contains a positive value tells me the smallest missing positive number, which is i + 1

        for i in range(sz):
            if nums[i] > 0:
                return i+1

        return sz + 1

