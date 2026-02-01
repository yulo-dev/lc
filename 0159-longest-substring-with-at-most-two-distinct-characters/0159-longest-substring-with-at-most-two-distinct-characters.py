class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # track: limit to two words, index
        # Invariant: the window contains at most two distinct characters.
        # Shrink trigger: if detect the third word in the window, shrink window
        # return max length

        left = 0
        count = {}
        best = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1

            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            best = max(best, right - left + 1)

        return best