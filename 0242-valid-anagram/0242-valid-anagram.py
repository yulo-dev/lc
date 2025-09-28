
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for s_ch in s:
            s_freq[s_ch] += 1

        for t_ch in t:
            t_freq[t_ch] += 1

        return s_freq == t_freq