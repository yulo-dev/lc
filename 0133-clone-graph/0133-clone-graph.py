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

        oldToNew = {} #key是原來的node, value是複製出來的new node
        oldToNew[node] = Node(node.val) #原節點 node → 複製節點 copy(node)
        queue = deque([node]) #放入起點

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                #(1)每拿到一個 nei（原圖鄰居），你先確保它有 clone（必要時建立）
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)   # “標記 visited” + “建立 clone”
                    queue.append(nei)
                #(2)最後把 clone(nei) 加進 clone(cur) 的 neighbors
                oldToNew[cur].neighbors.append(oldToNew[nei])  # 在「新圖」上建立同樣的邊

        return oldToNew[node]
