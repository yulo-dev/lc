class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if t not in operator:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(a / b))
        return stack[0]