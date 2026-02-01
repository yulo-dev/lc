class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        window = defaultdict(int) #ch -> occurrence
        best = 0
        left = 0

        for right, ch in enumerate(s):
            window[ch] += 1

            while len(window) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            best = max(best, right - left + 1)

        return best