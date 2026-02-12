class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        if target < nums[left] or target > nums[right]:
            return -1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid 
            else:
                right = mid 
                
        if target == nums[right]:
            return right
        elif target == nums[left]:
            return left
        else:
            return -1