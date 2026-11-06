class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        uni_nums = set(nums)
        cnt = 1
        res = 0

        for n in uni_nums:
            if n-1 not in uni_nums:
                cnt = 1
                
                while n+1 in uni_nums:
                    cnt += 1
                    n+=1
                res = max(res,cnt)

        return res
