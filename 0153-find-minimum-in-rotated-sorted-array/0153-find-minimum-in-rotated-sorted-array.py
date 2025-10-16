class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # 當只有一個元素
        if len(nums) == 1:
            return nums[0]

        # 用 left + 1 < right 避免無限循環
        while left + 1 < right:
            mid = (left + right) // 2

            # 若中間值大於右端，表示最小值在右邊
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        # 離開迴圈後，left 和 right 相鄰
        # 比較誰比較小
        return min(nums[left], nums[right])