"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_new = {}
        #左邊 old_new[node] → 把舊 node 當 key，新 node 當 value 存進 dict
        #右邊 Node(node.val) → 建一個全新的 Node，val 跟舊的一樣，但 neighbors 是空的 []
        old_new[node] = Node(node.val)
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in old_new:
                    old_new[nei] = Node(nei.val)
                    queue.append(nei)
                
                old_new[curr].neighbors.append(old_new[nei])

        return old_new[node]