class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = {}
        t2s = {}
        for s_ch, t_ch in zip(s, t):
            if s_ch not in s2t:
                s2t[s_ch] = t_ch
            if s2t[s_ch] != t_ch:
                return False

            if t_ch not in t2s:
                t2s[t_ch] = s_ch
            if t2s[t_ch] != s_ch:
                return False

        return True

