class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = defaultdict(int)
        res = 0
        
        for right, ch in enumerate(s):
            freq[ch] += 1
            
            while freq[ch] > 1: 
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res