class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        check = [0] * (n+1)
        res = []

        for num in nums:
            if check[num] == 0:
                check[num] = 1
            else:
                res.append(num)

        return res