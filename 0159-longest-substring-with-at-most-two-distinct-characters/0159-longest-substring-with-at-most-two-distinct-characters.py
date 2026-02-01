class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # track: limit to two words, index
        # Invariant: the window contains at most two distinct characters.
        # Shrink trigger: if detect the third word in the window, shrink window
        # return max length

        last_index = {} #ch->last index
        best = 0
        left = 0

        for right, val in enumerate(s):
            last_index[val] = right

            if len(last_index) > 2:
                drop = min(last_index, key=last_index.get)
                left = last_index[drop] + 1
                del last_index[drop]

            best = max(best, right - left + 1)

        return best