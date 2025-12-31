class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        visited = set()

        for right, val in enumerate(s):
            while val in visited:
                visited.remove(s[left])
                left += 1
                
            res = max(res, right - left + 1)
            visited.add(val)
        
        return res