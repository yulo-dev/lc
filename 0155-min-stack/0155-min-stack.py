class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = None

    def push(self, value: int) -> None:
        if self.min_num is None:
            self.min_num = value
        else:
            self.min_num = min(self.min_num, value)

        self.stack.append((value, self.min_num))

    def pop(self) -> None:
    
        self.stack.pop()

        if self.stack:
            _, self.min_num = self.stack[-1]
        else:
            self.min_num = None

    def top(self) -> int:
        val, _ = self.stack[-1]
        return val

    def getMin(self) -> int:
        _, min_num = self.stack[-1]
        return min_num


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()