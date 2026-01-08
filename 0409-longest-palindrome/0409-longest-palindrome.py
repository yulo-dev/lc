class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        cnt = Counter(s)
        total = 0
        odd = False

        for freq in cnt.values():
            total += (freq // 2) * 2
            if (freq % 2) == 1:
                odd = True
        
        if odd:
            total += 1

        return total