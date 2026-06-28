class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for i in range(len(s)):
            if stack and s[i] == stack[-1][0]:
                num, cnt = stack.pop()
                stack.append((num, cnt+1))
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append((s[i], 1))

        return ''.join(char * cnt for char, cnt in stack)
