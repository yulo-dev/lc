class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        left = 0
        freq = defaultdict(int)
        res = 0

        for right, ch in enumerate(s):
            while ch in freq:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            freq[ch] += 1
            res = max(res, right - left + 1)

        return res    