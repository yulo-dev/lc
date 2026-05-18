class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        visited = {} #char:index
        for right in range(len(s)):
            if s[right] in visited and visited[s[right]] < right:
                if visited[s[right]] >= left:
                    left = visited[s[right]] + 1
                visited[s[right]] = right 

            visited[s[right]] = right 
            res = max(res, right - left + 1)

        return res