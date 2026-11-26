class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        from collections import defaultdict

        left = 0
        right = 0
        window_freq = defaultdict(int)
        res = 0

        while right < len(s):
            window_freq[s[right]] += 1
            while window_freq[s[right]] > 1:
                window_freq[s[left]] -= 1
                if window_freq[s[left]] == 0:
                    del window_freq[s[left]]
                left += 1
        
            res = max(res, right - left + 1)
            right += 1

        return res
