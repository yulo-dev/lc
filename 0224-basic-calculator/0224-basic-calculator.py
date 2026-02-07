class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        sign = 1
        res = 0
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + (ord(ch) - ord("0"))

            elif ch in "+-":
                res += num * sign
                num = 0
                sign = 1 if ch == "+" else -1
            
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                num = 0 # optional
                sign = 1

            elif ch == ")":
                res += num * sign
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res = prev_res + prev_sign * res
                num = 0
                sign = 1 # optional

        res += num * sign

        return res