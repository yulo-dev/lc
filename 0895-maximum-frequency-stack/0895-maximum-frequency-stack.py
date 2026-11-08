class FreqStack:

    def __init__(self):
        
        self.freq = defaultdict(int)  #num and their frequency
        self.heap = [] #(-freq, ord, val)
        self.ord = 0

    def push(self, val: int) -> None:
        self.freq[val] -= 1
        self.ord -= 1
        heapq.heappush(self.heap, (self.freq[val], self.ord, val))

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.freq[val] += 1

        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()