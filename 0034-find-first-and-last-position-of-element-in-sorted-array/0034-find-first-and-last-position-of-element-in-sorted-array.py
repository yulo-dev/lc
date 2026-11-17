class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        #先找出leftmost
        left = 0
        right = len(nums)
        res = []

        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        if left == len(nums) or nums[left] != target:    
            return [-1, -1]
        else:
            res.append(left)


        #再找出rightmost
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        res.append(left-1)

        return res



        