class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}":"{", "]":"[", ")":"("}
        stack = []

        for ch in s:
            if ch in mapping:
                if not stack or mapping[ch] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack