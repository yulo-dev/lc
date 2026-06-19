class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            if value <= self.min_stack[-1]:
                self.min_stack.append(value)
    
    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            the_top = self.stack[-1]
            self.stack.pop()
            if the_top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        else:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()