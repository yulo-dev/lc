class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        cnt = 0

        for val in nums:
            if val % 3 != 0: #simplify this line bc we only have 3 condition for n % 3
                cnt += 1
        return cnt 
        