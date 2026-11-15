class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)

        if k == 0:
            return

        def reverse(left, right):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)

        