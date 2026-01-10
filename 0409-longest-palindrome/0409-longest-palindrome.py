class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_cnt = Counter(s)
        odd = False
        tot = 0

        for val in s_cnt.values():
            tot += (val // 2) * 2
            if (val % 2) == 1:
                odd = True
        
        if odd:
            tot += 1
        
        return tot