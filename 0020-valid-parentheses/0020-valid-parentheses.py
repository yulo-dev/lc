class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        bracket_map = {'}':'{', ']':'[', ')':'('}
        stack = []

        for ch in s:
            if ch in bracket_map:
                chk = stack.pop()
                if chk != bracket_map[ch]:
                    return False
            else:
                stack.append(ch)
        return stack == []