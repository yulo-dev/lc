class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        visited = {}
        
        for right, val in enumerate(s):
            if val in visited and visited[val] >= left:
                left = visited[val] + 1

            visited[val] = right
            res = max(res, right - left + 1)

        return res