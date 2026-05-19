class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        stack = []
        cnt = 0
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            elif ch == "+":
                num_sec = stack.pop()
                num_first = stack.pop()
                cnt = num_first + num_sec
                stack.append(cnt)
            elif ch == "-":
                num_sec = stack.pop()
                num_first = stack.pop()
                cnt = num_first - num_sec
                stack.append(cnt)
            elif ch == "*":
                num_sec = stack.pop()
                num_first = stack.pop()
                cnt = num_first * num_sec
                stack.append(cnt)
            elif ch == "/":
                num_sec = stack.pop()
                num_first = stack.pop()
                cnt = int(num_first / num_sec)
                stack.append(cnt)

        return stack[-1]
