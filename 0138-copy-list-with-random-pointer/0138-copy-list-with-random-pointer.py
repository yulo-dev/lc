"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # key = 舊節點的 reference（舊節點本人）
        # val = 我新建出來的 copy 節點
        # 加 {None: None} 是為了讓下面接指標時不用一直判斷 None
        oldToNew = {None: None}  

        # 1) copy all nodes (values only)
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        # 2) 用 oldToNew 來接 next/random（把"關係"接起來）
        # 不能在第一步驟就同時建立關係 因為在第一輪跑到某個 curr 時，curr.next 或 curr.random 指向的節點可能還沒被你建立分身，
        # 所以 oldToNew[curr.next]、oldToNew[curr.random] 可能不存在。
        curr = head
        while curr:
            copy = oldToNew[curr] # 拿到curr這個舊節點 然後透過oldToNew[curr] 去呼叫出他在第一輪建立的分身, 放進對應的新節點copy
            copy.next = oldToNew[curr.next] # 舊的 next 指到誰，新的一樣指到它的 copy
            copy.random = oldToNew[curr.random] # 舊的 random 指到誰，新的一樣指到它的 copy
            curr = curr.next

        return oldToNew[head]