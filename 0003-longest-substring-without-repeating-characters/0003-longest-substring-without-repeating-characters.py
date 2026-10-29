class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        res = 0
        window = defaultdict(int)

        while right < len(s):
            window[s[right]] += 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]] 
                left += 1
            
            res = max(res, right - left + 1)

            right += 1

        return res
