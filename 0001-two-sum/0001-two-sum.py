class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i, val in enumerate(nums):
            comp = target - val
            if comp in mapping:
                return [mapping[comp], i]
            mapping[val] = i