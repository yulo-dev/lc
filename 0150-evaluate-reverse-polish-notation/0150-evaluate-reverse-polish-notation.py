class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []

        for t in tokens:
            if t == "+":
                num_2 = stack.pop()
                num_1 = stack.pop()
                res = num_1 + num_2
                stack.append(res)

            elif t == "-":
                num_2 = stack.pop()
                num_1 = stack.pop()
                res = num_1 - num_2
                stack.append(res)

            elif t == "*":
                num_2 = stack.pop()
                num_1 = stack.pop()
                res = num_1 * num_2
                stack.append(res)

            elif t == "/":
                num_2 = stack.pop()
                num_1 = stack.pop()
                res = int(num_1 / num_2)
                stack.append(res)
            
            else:
                stack.append(int(t))

        return stack[-1]
