class RandomizedSet:

    def __init__(self):
        self.val_to_index = defaultdict(list)
        self.index_to_val = defaultdict(list)
        self.cnt = 0

    def insert(self, val: int) -> bool:
        if val not in self.val_to_index:
            self.val_to_index[val] = self.cnt 
            self.index_to_val[self.cnt] = val
            self.cnt += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.val_to_index:
            idx = self.val_to_index[val]
            last_val = self.index_to_val[self.cnt - 1]

            self.index_to_val[idx] = last_val
            del self.index_to_val[self.cnt - 1]

            self.val_to_index[last_val] = idx
            del self.val_to_index[val]

            self.cnt -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        import random
        idx = random.randint(0, self.cnt -1)
        return self.index_to_val[idx]


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()