class Solution:
    def isValid(self, s: str) -> bool:
        
        mapping = {")": "(", "}": "{", "]": "[" }

        stack = []

        for ch in s:
            if ch in mapping:
                if not stack or (stack[-1] != mapping[ch]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0 