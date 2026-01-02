class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        left = 0
        last = {}

        for right, val in enumerate(s):
            if val in last and last[val] >= left:
                left = last[val] + 1

            last[val] = right
            res = max(res, right - left + 1)
        
        return res