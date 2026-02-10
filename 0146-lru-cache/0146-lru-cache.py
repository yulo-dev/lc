# get要 O(1) 所以用hashmap去存: 存key - > node 這樣get(key) 才會是O(1) 拿到那個node
# DLL 才可以讓remove & move to front 都 O(1) 
# SLL 要把中間某個node拿出來 需要知道他的前一個 常常會 O(n)

# 總結
# dict 解決：key -> node 的 O(1) 存取
# DLL 解決：維護「最近使用順序」的 O(1) 移動/刪除
# → 兩個合起來才做得到 get/put 都 O(1)

class Node:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {} # key -> node
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.next = self.head

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node):
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def _move_to_front(self, node):
        self._remove(node)
        self._add_to_front(node)

    def _remove_lru(self):
        lru = self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key):
        if key not in self.map:
            return -1

        node = self.map[key]
        self._move_to_front(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            node = self.map[key]
            node.val = val
            self._move_to_front(node)
            return

        node = Node(key, val)
        self.map[key] = node
        self._add_to_front(node)

        if len(self.map) > self.cap:
            lru = self._remove_lru()
            del self.map[lru.key]

        


        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)






# design a Node class for cache: double linkedlist so that put & get can be O(1)
# within LRUCache: create map, prev, next, in map, key = node, val = node.val