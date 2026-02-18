"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque([root])

        while queue:
            # 關鍵：一定要先固定這一層的長度！
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # 如果不是這一層的最後一個，就連向 Queue 的頭
                if i < level_size - 1:
                    node.next = queue[0]

                # 正常加入下一層的小孩
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root