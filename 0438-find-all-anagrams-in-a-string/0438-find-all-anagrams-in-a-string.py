class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        
        left = 0
        right = 0

        need = defaultdict(int)
        window = defaultdict(int)

        res = []

        for ch in p:
            need[ch] += 1

        while right < len(s):

            if s[right] in need:
                window[s[right]] += 1

            right += 1

            while (right - left) > len(p):

                if s[left] in need:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]

                left += 1

            if window == need:
                res.append(left)

        return res