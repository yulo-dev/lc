class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True

        i = 0

        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
                if i == len(s):
                    return True
        
        return False