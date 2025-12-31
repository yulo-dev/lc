class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = {}

        for i, val in enumerate(nums):
            comp = target - val
            if val in mapping:
                return [mapping[val], i]
            else:
                mapping[comp] = i