class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        cnt = 0

        for n in nums:
            cnt = max(n, cnt + n) # 要嘛重開，要嘛接上去
            res = max(res, cnt)
        
        return res