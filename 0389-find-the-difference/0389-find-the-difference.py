class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)

        for ch in t_dict:
            if t_dict[ch] != s_dict.get(ch, 0):
                return ch