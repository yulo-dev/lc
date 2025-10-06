class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = defaultdict(int)
        t_cnt = defaultdict(int)

        for ch in s:
            s_cnt[ch] += 1
        for ch in t:
            t_cnt[ch] += 1

        return s_cnt == t_cnt
