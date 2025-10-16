class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0    
        left = 0
        visited = set()

        for right, ch in enumerate(s):
            while ch in visited:
                visited.remove(s[left])
                left += 1
            visited.add(ch)
            res = max(res, right - left + 1)

        return res