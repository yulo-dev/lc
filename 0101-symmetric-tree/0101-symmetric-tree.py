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
            a, b = queue.popleft()

            if not a and not b:
                continue
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False

            queue.append((a.left, b.right))
            queue.append((b.left, a.right))

        return True