class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        prefix = [1] * (n+1)
        suffix = [1] * (n+1)

        # Prefix：從左往右
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] * nums[i-1]

        # Suffix：從右往左
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        #res
        res = [0] * (n)
        for i in range(n):
            res[i] = prefix[i] * suffix[i+1]

        return res

    
