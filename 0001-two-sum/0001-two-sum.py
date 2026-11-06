class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        from collections import defaultdict

        mapping = defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in mapping:
                return [mapping[target - num], i]
            else:
                mapping[num] = i
        return []