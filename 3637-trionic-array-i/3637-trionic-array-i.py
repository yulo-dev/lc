class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        i = 0

        # 1) first part: strictly increasing
        # 
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # first part must be non-empty, and cannot end at last index
        if i == 0 or i == n - 1:
            return False

        # 2) second part: strictly decreasing
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1

        # second part must be non-empty, and cannot end at last index
        if j == i or j == n - 1:
            return False

        # 3) third part: strictly increasing
        while j + 1 < n and nums[j] < nums[j + 1]:
            j += 1

        return j == n - 1