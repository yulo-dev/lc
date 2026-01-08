class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        cnt = 0

        for n in nums:
            if cnt < 0:
                cnt = 0
            cnt += n
            res = max(res, cnt)
        
        return res