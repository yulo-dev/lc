class Solution:
    def isValid(self, s: str) -> bool:
        collection = {"]":"[", ")":"(", "}":"{"}
        stack = []

        for ch in s:
            if ch in collection:
                if not stack or stack[-1] != collection[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack