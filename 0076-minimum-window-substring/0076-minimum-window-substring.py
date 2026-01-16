class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        t_cnt = Counter(t)
        window = Counter()

        formed = 0

        left = 0
        best_len = float("inf")
        best_left = 0

        for right, val in enumerate(s):
            
            window[val] += 1

            if val in t_cnt and window[val] == t_cnt[val]:
                formed += 1

            while formed == len(t_cnt):

                if (right - left + 1) < best_len:
                    best_len = right - left + 1
                    best_left = left

                window[s[left]] -= 1

                if s[left] in t_cnt and window[s[left]] < t_cnt[s[left]]:
                    formed -= 1
                
                left += 1
            
        if best_len == float("inf"):
            return ""
        else:
            return s[best_left:best_left + best_len]