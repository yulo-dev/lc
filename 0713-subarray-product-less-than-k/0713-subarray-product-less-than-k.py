class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:

        if k <= 1:
            return 0
        
        left = 0
        right = 0
        res = 0
        tot = 1

        while right < len(nums):
            
            tot *= nums[right]
            right += 1

            while left < right and tot >= k:
                tot //= nums[left]
                left += 1

            res += right - left 

        return res

        

            

