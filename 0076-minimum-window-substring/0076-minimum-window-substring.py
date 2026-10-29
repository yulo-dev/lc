class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #move right: when the window does not contain all the character in t
        #move left: when the window contain all the character in t (try to shrink th window and find the mininum length)
        #update result: every time the window is valid, BEFORE shrinking left

        from collections import defaultdict

        need = defaultdict(int)
        for ch in t:
            need[ch] += 1

        window = defaultdict(int)

        left = 0 
        right = 0 

        valid = 0

        res = ""

        while right < len(s):
            if s[right] in need:
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    valid += 1
            
            right += 1

            while left < right and valid == len(need):
                
                if len(res) == 0 or (right - left < len(res)):
                    res = s[left:right]

                if s[left] in window:
                    window[s[left]] -= 1

                    if window[s[left]] < need[s[left]]:
                        valid -= 1

                    if window[s[left]] == 0:
                        del window[s[left]]
                        

                left += 1

        return res