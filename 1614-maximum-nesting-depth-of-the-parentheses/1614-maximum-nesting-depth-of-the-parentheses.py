class Solution:
    def maxDepth(self, s: str) -> int:

        depth = 0
        res = 0 

        for ch in s:
            if ch == "(":
                depth += 1

            elif ch == ")":
                res = max(res, depth)
                depth -= 1

            else:
                continue

        return res