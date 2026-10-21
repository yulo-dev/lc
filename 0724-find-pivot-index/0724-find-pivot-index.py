class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        

        prefix = [0] * (len(nums) + 1)
      
        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(len(nums)):
            left = prefix[i] 
            right = prefix[-1] - prefix[i+1] 

            if right == left:
                return i

        return -1

        


        