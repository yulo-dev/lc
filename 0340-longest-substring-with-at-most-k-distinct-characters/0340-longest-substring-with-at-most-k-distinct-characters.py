class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        window = {}
        best = 0
        left = 0

        for right, ch in enumerate(s):
            window[ch] = right

            if len(window) > k:
                drop_ch = min(window, key=window.get)
                left = window[drop_ch] + 1
                del window[drop_ch]

            best = max(best, right - left + 1)

        return best