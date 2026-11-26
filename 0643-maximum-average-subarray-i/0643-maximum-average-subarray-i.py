class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        window = sum(nums[0:k])
        res = window 

        for i in range(k,len(nums)):
            window += (nums[i] - nums[i-k])
            res = max(res, window) 

        return res / k