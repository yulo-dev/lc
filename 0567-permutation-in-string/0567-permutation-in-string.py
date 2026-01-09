class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window = Counter()
        left = 0

        for right, val in enumerate(s2):
            window[val] += 1

            if (right - left + 1) > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            
            if (right - left + 1) == len(s1) and window == s1_count:
                return True

        return False