class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)

        for ch in t_dict:
            if ch not in s_dict:
                return ch
            elif t_dict[ch] != s_dict[ch]:
                return ch