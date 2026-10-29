class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        right = 0
        freq = defaultdict(int)
        max_freq = 0
        res = 0

        while right < len(s):

            freq[s[right]] += 1

            max_freq = max(max_freq, freq[s[right]])

            right += 1

            while right - left - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                max_freq = max(freq.values())

            res = max(res, right - left)

        return res