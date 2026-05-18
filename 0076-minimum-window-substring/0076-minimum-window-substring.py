class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        left = 0
        window_freq = defaultdict(int)
        t_freq = Counter(t)
        min_len = float("inf")
        res = ""

        for right in range(len(s)):
            window_freq[s[right]] += 1
            while self.is_valid(window_freq, t_freq):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]

                window_freq[s[left]] -= 1
                left += 1

        return res

    def is_valid(self, window_freq, t_freq):
        for ch, freq in t_freq.items():
            if ch not in window_freq or freq > window_freq[ch]:
                return False
        return True