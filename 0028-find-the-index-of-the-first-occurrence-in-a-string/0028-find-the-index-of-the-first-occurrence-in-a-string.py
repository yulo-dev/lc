class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        if len(needle) > len(haystack):
            return -1

        hay_n = len(haystack)
        needle_n = len(needle)

        for i in range(0, hay_n - needle_n + 1):
            if haystack[i:i + needle_n] == needle:
                return i
            
        return -1