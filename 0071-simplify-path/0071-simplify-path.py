class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        componenet = path.split("/")

        for ch in componenet:
            if ch == "" or ch == ".":
                continue
            elif ch == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return "/" + "/".join(stack)