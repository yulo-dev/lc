from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > 1:
                return True
        return False