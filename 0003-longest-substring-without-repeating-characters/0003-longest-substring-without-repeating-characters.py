class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window
        #left, right pointers as the window boundaries
        #if the window does't have repeat character: kepp exapnd it by moving right pointer ---->
        #if the window have repeat character: remove the old one at leftmost 
        #keep track of the maximum length as the window changes

        left = 0
        res = 0
        visited = defaultdict(int)
        for right, ch in enumerate(s):
            while ch in visited:
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    del visited[s[left]] 
                left += 1
            visited[ch] += 1
            res = max(res, right - left + 1)
        return res