class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right] #停下來的那一刻，left/right 指向的是“不合法”的那格, 所以「真正最後一次合法的回文」是在它的內側一格。

        res = ""
        for i in range(len(s)):
            odd = expand(i,i)
            if len(odd) > len(res):
                res = odd
            
            even = expand(i,i+1)
            if len(even) > len(res):
                res = even

        return res