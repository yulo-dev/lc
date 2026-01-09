class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        left = 0
        s1_cnt = Counter(s1)
        window = Counter()
        
        for right, val in enumerate(s2):
            window[val] += 1

            if (right- left + 1) > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]]  == 0:
                    del window[s2[left]] 
                left += 1
            
            if (right- left + 1) == len(s1) and s1_cnt == window:
                return True

        return False