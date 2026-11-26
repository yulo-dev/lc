class ListNode:
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapping = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head 

    def _remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def _add(self, node):
        node.next = self.head.next 
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        
        node = self.mapping[key]

         # 1. 從原本位置移除 node：移除的話兩條線 兩個關係要寫
        self._remove(node)

        # 2. 插入 head 後面（MRU）: 插入的話四條線 四個關係都要寫
        self._add(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            old_node = self.mapping[key] 
            old_node.val = value
            self._remove(old_node)
            self._add(old_node)
        else:
            node = ListNode(key, value)
            self._add(node)
            self.mapping[key] = node

        if len(self.mapping) > self.cap:
            extra_node = self.tail.prev
            extra_key = extra_node.key
            del self.mapping[extra_key]

            self._remove(extra_node)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)