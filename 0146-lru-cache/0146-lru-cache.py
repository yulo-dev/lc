class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

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

    def _pop_lru(self):
        lru = self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._move_to_front(node)
        return node.val

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._move_to_front(node)
            return
        
        node = Node(key, value)
        self.map[key] = node
        self._add_to_front(node)

        if len(self.map) > self.cap:
            lru = self._pop_lru()
            del self.map[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)