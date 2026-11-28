class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        
        for ch in s:
            if ch == "(":
                stack.append(ch)

            else:
                if not stack:
                    res += 1
                else:
                    stack.pop()
        
        while stack:
            res += 1
            stack.pop()

        return res