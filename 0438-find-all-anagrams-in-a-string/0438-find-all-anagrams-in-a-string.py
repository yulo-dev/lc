class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_cnt = Counter(p)
        window = Counter()
        left = 0
        res = []

        for right, val in enumerate(s):
            window[val] += 1

            if (right - left + 1) > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]] 
                left += 1

            if (right - left + 1) == len(p) and window == p_cnt:
                res.append(left)

        return res