class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = nums[0]

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0  #清空cur_sum, 重頭來過
            cur_sum += n 
            max_sum = max(max_sum, cur_sum)

        return max_sum
