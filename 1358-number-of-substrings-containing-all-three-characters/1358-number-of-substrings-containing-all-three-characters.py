class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        freq = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            freq[s[right]] += 1

            while freq['a'] >= 1 and freq['b'] >= 1 and freq['c'] >= 1:
                res += len(s) - right
                freq[s[left]] -= 1
                left += 1
                

        return res