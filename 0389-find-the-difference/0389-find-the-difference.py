class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)

        if s == "":
            return t

        for t in t_dict:
            if t not in s_dict:
                return t
            elif t_dict[t] != s_dict[t]:
                return t