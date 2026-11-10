class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        uni_nums = set(nums)
        res = 0

        for n in uni_nums:

            if n-1 not in uni_nums:
                start = n
                cnt = 1

                while start+1 in uni_nums:
                    cnt += 1
                    start = start + 1

                res = max(res, cnt)

        return res