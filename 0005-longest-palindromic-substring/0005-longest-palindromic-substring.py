class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]

        res = []
        for i in range(len(s)):
            odd_word = expand(i, i)
            if len(odd_word) > len(res):
                res = odd_word

            even_word = expand(i, i+1)
            if len(even_word) > len(res):
                res = even_word
        return res
            