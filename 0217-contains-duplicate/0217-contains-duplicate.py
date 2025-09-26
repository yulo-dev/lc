from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for i in cnt.values():
            if i > 1:
                return True
        return False