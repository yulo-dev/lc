class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # 最大環狀和 = totalSum - 最小連續子陣列和
        # 全負數: 如果 maxSubarray < 0 → 直接回傳 maxSubarray

        total = 0

        cur_max = 0
        max_sum = nums[0]

        cur_min = 0
        min_sum = nums[0]

        for x in nums:
            total += x

            # Kadane for max subarray
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)

            # Kadane for min subarray
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)

        # all negative: cannot take empty subarray
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)


# 環狀最大子陣列只有兩種可能：
# 不跨尾頭（normal）：就是一般的 maximum subarray → Kadane max
# 跨尾頭（wrap-around）：等價於「總和 - 中間被排除的一段最小子陣列」

# 所以
# Case 1 (non-circular): run Kadane to get max_sum
# Case 2 (circular): compute total - min_sum where min_sum is min subarray sum (Kadane variant)
# Edge case: if all numbers are negative, return max_sum (avoid empty subarray)