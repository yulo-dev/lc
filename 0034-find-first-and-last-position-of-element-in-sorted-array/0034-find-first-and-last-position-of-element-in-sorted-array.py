class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        if n == 0:
            return [-1, -1]
        
        def find_leftmost():
            left = 0 
            right = len(nums)

            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        def find_rightmost():
            left = 0 
            right = len(nums)

            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1

            return left

        l = find_leftmost()
        if not (0 <= l < n) or nums[l] != target:
            return [-1, -1]
        r = find_rightmost() - 1

        return [l, r]