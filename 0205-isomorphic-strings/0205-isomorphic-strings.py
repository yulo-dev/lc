class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s2t = {}
        t2s = {}

        for s_ch, t_ch in zip(s, t):
            if s_ch in s2t and s2t[s_ch] != t_ch:
                return False
            if t_ch in t2s and t2s[t_ch] != s_ch:
                return False

            s2t[s_ch] = t_ch
            t2s[t_ch] = s_ch

        return True