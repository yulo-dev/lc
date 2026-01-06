class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in mapping:
                return [mapping[comp], i]
            mapping[num] = i