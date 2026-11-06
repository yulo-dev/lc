class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for ch in s:
            s_freq[ch] += 1
        
        for ch in t:
            t_freq[ch] += 1

        return s_freq == t_freq