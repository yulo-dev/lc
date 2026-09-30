class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        uni_nums = sorted(set(nums))
        length = 1
        res = 1

        for i in range(len(uni_nums)):
            if i > 0 and uni_nums[i] - uni_nums[i-1] == 1:
                length += 1
                res = max(res, length)
            else:
                length = 1

        return res
