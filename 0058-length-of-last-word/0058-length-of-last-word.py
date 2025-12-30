class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        temp = 0
        ans = 0

        if not s:
            return res

        for ch in s:
            if ch == " ":
                temp = 0
            else:
                temp += 1
                ans = temp

        return ans