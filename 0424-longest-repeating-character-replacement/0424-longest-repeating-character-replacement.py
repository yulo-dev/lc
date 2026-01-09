class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxfreq = 0
        res = 0

        for right, val in enumerate(s):
            count[val] += 1
            maxfreq = max(maxfreq, count[val])

            while (right - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res                