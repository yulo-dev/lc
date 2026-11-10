class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        mapping = defaultdict(int) #key = nums - target #val = index
        res = []
        for i in range(len(nums)):
            if target - nums[i] in mapping:
                return [mapping[target - nums[i]], i]
            else:
                mapping[nums[i]] = i
