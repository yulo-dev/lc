class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        right = 0

        window = {}

        while right < len(nums):

            if nums[right] in window:
                if right - window[nums[right]] <= k:
                    return True
            
            window[nums[right]] = right
             
            right += 1

        return False
