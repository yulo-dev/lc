class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)

        for i, ch in enumerate(s):
            if cnt[ch] == 1: 
                return i
                break
        return -1