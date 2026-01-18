class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        component = path.split("/")

        for c in component:
            if c == "" or c == ".":
                continue
            elif c == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return "/" + "/".join(stack)