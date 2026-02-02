class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        ans = 0
        n = len(s)

        for i in range(n):
            cur = mapping[s[i]]
            if i + 1 < n and cur < mapping[s[i+1]]:
                ans -= cur
            else:
                ans += cur

        return ans