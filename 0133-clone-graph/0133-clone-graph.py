"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#要複製
    #node的value
    #neighbor關係
    #整個graph structure

#核心考點
    #graph不是tree, 他有cycle 或可能 多個node指向同個node
    #需要用hashmap 其中key=舊的node value=對應的新的clone node 
    #hashmap用來防止
        #重複clone
        #防止cycle



from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # use bfs or dfs to traverse the original graph, and use a hashmap to store a mapping from the original node to its cloned node
        # use a queue to store the current node
        # bfs
        # traverse its neighbor
            # if the neighbor hasn't been add in the map: add in the map & queue
        # connect the new cloned node with new cloned neighbor
        # return the cloned starting node

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
                    queue.append(nei) # 原本graph的neighbor node
                
                oldtonew[curr].neighbors.append(oldtonew[nei])

        return oldtonew[node]