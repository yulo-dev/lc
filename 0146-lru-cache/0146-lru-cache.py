class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        #dll
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {} #key -> Node
        #dummy head & tail
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_start(self, node):
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        first.prev = node

    def _move_to_start(self, node):
        self._remove(node)
        self._add_to_start(node)

    def _lru_remove(self):
        lru = self.tail.prev
        self._remove(lru)
        return lru

    def get(self, key):
        if key not in self.map:
            return -1

        node = self.map[key]
        self._move_to_start(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            node = self.map[key]
            node.val = val
            self._move_to_start(node)
            return
        
        node = Node(key, val)
        self.map[key] = node
        self._add_to_start(node)
        if len(self.map) > self.cap:
            lru = self._lru_remove()
            del self.map[lru.key]

