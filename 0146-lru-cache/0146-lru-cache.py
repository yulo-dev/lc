class Node:
    def __init__(self, key, val):
        self.key = key # 建立就一定要有 → 放參數 #node 存 key，是為了在淘汰時能用 lru.key 立刻從 dict 刪掉那筆資料，保持 O(1)
        self.val = val # 建立就一定要有 → 放參數
        self.prev = None # 一開始不一定知道 → 先給合法初值
        self.next = None # 一開始不一定知道 → 先給合法初值

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {} # key -> Node

        #dummy nodes
        self.head = Node(0,0)
        self.tail = Node(0,0)
        #head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node):
        #拔掉前：prev <-> node <-> nxt
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        #最後變成：prev <-> nxt

    def _add_to_front(self, node):
        first = self.head.next #用來暫存原本的第一個node 現在要被往後移了
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)

    def _pop_lru(self):
        lru = self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key] #前面的設計就是這邊dictionary 是key對應node
        self._move_to_front(node)
        return node.val #然後node裡面才存value, 以及key, prev, next

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._move_to_front(node)
            return

        node = Node(key, value) #建立node
        self.map[key] = node #把node登記到dict
        self._add_to_front(node)

        if len(self.map) > self.cap:
            lru = self._pop_lru()  #這邊拿到的是node：從 linked list 移除並回傳 LRU 節點（Node）
            del self.map[lru.key]  #要抓出node的key 才能刪dictionary：用該節點的 key 從 dictionary 同步刪除索引，確保兩個結構一致


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)