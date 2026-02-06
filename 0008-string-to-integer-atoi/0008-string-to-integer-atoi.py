class Solution:
    def myAtoi(self, s: str) -> int:

        n = len(s)
        i = 0

        # 1) skip leading spaces
        while i < n and s[i] == " ":
            i += 1
        if i == n:
            return 0

        # 2) sign
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        # 3) read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0") #把文字數字轉成真的數字 #也可以用digit = int(s[i])
            num = num * 10 + digit
            i += 1

        num *= sign

        # 4) clamp to 32-bit signed range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
