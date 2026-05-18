class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        left = 0
        window_freq = defaultdict(int)
        t_freq = Counter(t)
        min_len = float("inf")
        res = ""
        comp = 0

        for right in range(len(s)):
            window_freq[s[right]] += 1

            if s[right] in t_freq and window_freq[s[right]] == t_freq[s[right]]:
                comp += 1

            while comp >= len(t_freq):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]

                window_freq[s[left]] -= 1
                if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                    comp -= 1
                left += 1

        return res