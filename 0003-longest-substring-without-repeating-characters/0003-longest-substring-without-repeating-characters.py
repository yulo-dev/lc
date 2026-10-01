class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        window = set()
        res = 0

        for i in range(len(s)):
            right = i

            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])
            res = max(res, len(window))

        return res