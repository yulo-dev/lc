class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        hay_n = len(haystack)
        needle_n = len(needle)

        if needle_n > hay_n:
            return -1

        for i in range(0, hay_n - needle_n + 1):
            j = 0
            while (j < needle_n):
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == needle_n:
                return i
            
        return -1