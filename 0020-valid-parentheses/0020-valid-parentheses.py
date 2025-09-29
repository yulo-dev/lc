class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = {'}':'{', ']':'[', ')':'('}
        stack = []

        for ch in s:
            if ch in bracket_map:
                if not stack or stack[-1] != bracket_map[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack