class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = [] #depth: everytime we meet the open bracket we will add one
        depth = 0
        stack.append(depth)

        res = 0 

        for ch in s:
            if ch == "(":
                depth = stack[-1] + 1
                stack.append(depth)
            elif ch == ")":
                depth = stack.pop()
                res = max(res, depth)
            else:
                continue

        return res

        