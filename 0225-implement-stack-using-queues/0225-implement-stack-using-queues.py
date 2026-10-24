from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_element = None
        
    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_element = x

    def pop(self) -> int:
        length = len(self.q)
        while length > 2:
            self.q.append(self.q.popleft())
            length -= 1
        
        self.top_element = self.q[0] #關鍵
        self.q.append(self.q.popleft()) 

        return self.q.popleft()

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()