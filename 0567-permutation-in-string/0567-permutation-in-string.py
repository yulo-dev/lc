class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        left = 0
        right = 0

        need = defaultdict(int)
        window = defaultdict(int)

        for ch in s1:
            need[ch] += 1

        while right < len(s2):

            if s2[right] in need:
                window[s2[right]] += 1

            right += 1

            while (right - left) > len(s1):
                if s2[left] in need:
                    window[s2[left]] -= 1
                    if window[s2[left]] == 0:
                        del window[s2[left]]

                left += 1

            if window == need:
                return True

        return False