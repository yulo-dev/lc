class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}  # val -> index in arr 

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        # 為了list要用pop 維持O(1) 所以把最後一個元素 last 搬去補你要刪的位置 idx, 這樣要刪的元素就被覆蓋掉了，最後再 pop() 掉尾巴（O(1)）
        index = self.pos[val]
        last = self.arr[-1]

        # move last to idx
        self.arr[index] = last
        self.pos[last] = index

        # pop last and delete val
        self.arr.pop() 
        del self.pos[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()