class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "]":"[", "}":"{"}
        stack = []
        for ch in s:
            if ch in mapping and stack:
                top = stack.pop()
                if mapping[ch] != top:
                    return False
            else:
                stack.append(ch)
        return not stack