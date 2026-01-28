class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        #DLL
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

    def _add_to_start(self, node):
        first = self.head.next
        node.next = first
        node.prev = self.head
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

      

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)






# design a Node class for cache: double linkedlist so that put & get can be O(1)
# within LRUCache: create map, prev, next, in map, key = node, val = node.val