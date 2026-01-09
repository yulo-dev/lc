class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        maxfreq = 0
        s_cnt = defaultdict(int)

        for right, val in enumerate(s):
            s_cnt[val] += 1
            maxfreq = max(maxfreq, s_cnt[val])

            while (right - left + 1) - maxfreq > k:
                 s_cnt[s[left]] -= 1
                 left += 1

            res = max(res, right- left + 1)
        
        return res