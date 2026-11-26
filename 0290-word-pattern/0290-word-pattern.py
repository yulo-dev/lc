class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if len(pattern) != len(s.split()):
            return False

        p2ch = {}
        ch2p = {}

        for p, ch in zip(pattern, s.split()):
            if p not in p2ch:
                p2ch[p] = ch
            if p2ch[p] != ch:
                return False

            if ch not in ch2p:
                ch2p[ch] = p
            if ch2p[ch] != p:
                return False

        return True

