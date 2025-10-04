class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        visit = defaultdict(int)
        for right, ch in enumerate(s):
            while ch in visit:
                visit[s[left]] -= 1
                if visit[s[left]] == 0:
                    del visit[s[left]]
                left += 1

            visit[ch] += 1
            res = max(res, right - left + 1)

        return res