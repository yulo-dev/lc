class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 
        mapping = {}
        res = 0

        for right, ch in enumerate(s):
            if ch in mapping:
                if left <= mapping[ch]:
                    left = mapping[ch] + 1

            mapping[ch] = right
            res = max(res, right - left + 1)

        return res
