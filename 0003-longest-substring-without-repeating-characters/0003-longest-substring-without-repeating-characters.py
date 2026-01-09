class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        seen = {}

        for right, val in enumerate(s):
            if val in seen and seen[val] >= left:
                left = seen[val] + 1

            seen[val] = right
            res = max(res, right - left + 1)

        return res