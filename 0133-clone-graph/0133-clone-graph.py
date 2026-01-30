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

        oldtonew = {}
        oldtonew[node] = Node(node.val)
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in oldtonew:
                    oldtonew[nei] = Node(nei.val)
                    queue.append(nei)
            
                #在複製圖裡，把 curr' -> nei' 這條邊接起來:
                    #oldtonew[curr]：拿到「curr 這個原本節點」對應的「複製節點 curr'」
                    #oldtonew[nei]：拿到「nei 這個原本鄰居節點」對應的「複製節點 nei'」
                    #append(...)：在 curr' 的 neighbors 裡加入 nei'
                #為什麼不能寫 curr.neighbors.append(nei)
                    #curr 是 原圖的節點
                    #nei 是 原圖的鄰居
                    #curr.neighbors.append(nei) 會把邊加在 原圖 上
                oldtonew[curr].neighbors.append(oldtonew[nei])

        return oldtonew[node] 

