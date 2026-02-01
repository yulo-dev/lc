class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]
        curr_min = sum_min = nums[0]
        curr_max = sum_max = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            total += x

            curr_min = min(x, curr_min + x)
            sum_min = min(sum_min, curr_min)

            curr_max = max(x, curr_max + x)
            sum_max = max(sum_max, curr_max)

        #sum_max 是「最大非空子陣列和」。如果它都小於 0，代表連選單一元素都小於 0 → 全負
        #不是用total
        if sum_max < 0:
            return sum_max

        return max(sum_max, total - sum_min)