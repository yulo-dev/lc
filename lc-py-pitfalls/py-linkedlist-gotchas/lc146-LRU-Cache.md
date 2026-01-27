LRU Cache needs two things at the same time: O(1) lookup by key and O(1) updates to recency order. A single data structure can’t do both efficiently, so I combine a hash map with a doubly linked list.

The hash map stores key -> node, so get and put can locate the node in O(1). The doubly linked list maintains usage order: the most recently used item is near the head, and the least recently used item is near the tail. I use dummy head and tail to make insert/remove operations constant time.

For get(key), if the key exists, I move that node to the head and return its value; otherwise return -1.
For put(key, value), if the key already exists, I update node.value and move it to the head. If it doesn’t exist, I create a new node, add it to the head, and record it in the map. If capacity is exceeded, I evict tail.prev (the least recently used node) from the list and delete its key from the map.

All operations are O(1) time, and space is O(capacity).
