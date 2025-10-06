class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        res = 0
        visited = defaultdict(int)

        for right in range(len(s)):
            while s[right] in visited:
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    del visited[s[left]]
                left += 1

            visited[s[right]] += 1

            res = max(res, right - left + 1)

        return res