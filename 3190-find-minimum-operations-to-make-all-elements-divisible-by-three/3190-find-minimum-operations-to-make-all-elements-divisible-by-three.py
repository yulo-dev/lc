class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        cnt = 0

        for val in nums:
            if (val + 1) % 3 == 0 or (val - 1) % 3 == 0:
                cnt += 1
        return cnt 
        