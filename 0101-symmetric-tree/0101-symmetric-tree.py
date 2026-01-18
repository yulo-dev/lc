# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:

            node_left, node_right = queue.popleft()

            if not node_left and not node_right:
                continue
            if not node_left or not node_right:
                return False
            if node_left.val != node_right.val:
                return False

            queue.append((node_left.left, node_right.right))
            queue.append((node_left.right, node_right.left))

        return True
            