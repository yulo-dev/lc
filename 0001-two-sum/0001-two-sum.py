class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # mapping: {key: value}; key = target - current value; value = index
        # for loop to iterate through the nums
        # if value in mapping: append result
        # if not, store the info in mapping 

        mapping = {}
        
        for i, val in enumerate(nums):
            comp = target - val
            if comp in mapping:
                return [mapping[comp], i]
            
            mapping[val] = i
        
        return res