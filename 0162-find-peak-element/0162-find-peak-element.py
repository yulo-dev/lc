class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid+1]: #右邊在上坡，peak 一定在右半邊
                left = mid
            else: #右邊在下坡或轉折，peak 一定在左半邊
                right = mid

        if nums[left] > nums[right]:
            return left
        else:
            return right