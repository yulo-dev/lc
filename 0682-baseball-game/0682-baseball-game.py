class Solution:
    def calPoints(self, operations: list[str]) -> int:
        
        stack = []

        for op in operations:
            if op == "+":
                tot = 0
                num1 = int(stack[-1]) if stack else 0
                num2 = int(stack[-2]) if stack else 0
                tot = num1 + num2
                stack.append(tot)
            elif op == "C":
                stack.pop() 
            elif op == "D":
                num = int(stack[-1]) * 2
                stack.append(num)
            else:
                stack.append(int(op))

        res = 0
        while stack:
            num = stack.pop()
            res += num

        return res
