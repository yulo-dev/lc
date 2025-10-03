class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r] #因為 while loop 結束時，l 和 r 已經走到錯的地方了：l 少了一步（多減 1） 或 r 多了一步（多加 1）

        result = ""  # Store the longest palindrome substring

        # Iterate over each index to check every possible center
        for i in range(len(s)):
            # Case 1: Odd-length palindrome (center at one character)
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1  # Update result if longer palindrome is found

            # Case 2: Even-length palindrome (center between two characters)
            sub2 = expand(i, i + 1)
            if len(sub2) > len(result):
                result = sub2  # Update result if longer palindrome is found

        return result  # Return the longest palindrome substring found