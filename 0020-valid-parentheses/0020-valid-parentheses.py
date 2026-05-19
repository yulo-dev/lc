class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] # store the open brackets
        mapping = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in mapping:
                if not stack or mapping[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(ch)

        return len(stack) == 0


    