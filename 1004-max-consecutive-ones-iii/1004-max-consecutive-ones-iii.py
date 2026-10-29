class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

        #extend right: k > 0
        #extend left: k < 0
        #update res: k > 0 
      

        left = 0 
        right = 0

        res = 0

        while right < len(nums):
            
            if nums[right] == 0:
                k -= 1
            right += 1

            if k >= 0:
                res = max(res, right - left)

            while left < right and k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
                
        return res