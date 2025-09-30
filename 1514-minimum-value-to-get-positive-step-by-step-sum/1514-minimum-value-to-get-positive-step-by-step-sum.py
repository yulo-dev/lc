class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        tot = 0
        min_tot = 0

        for num in nums:
            tot += num
            min_tot = min(min_tot, tot)

        if min_tot < 0:
            return abs(min_tot) + 1
        else:
            return 1
