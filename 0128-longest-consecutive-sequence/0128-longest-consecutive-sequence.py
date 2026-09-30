class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        uni_nums = set(nums)
        res = 0

        for n in uni_nums:
            if n - 1 not in uni_nums:
                length = 1
                start = n

                while start + 1 in uni_nums:
                    start = start + 1
                    length += 1

                res = max(res, length)

        return res
