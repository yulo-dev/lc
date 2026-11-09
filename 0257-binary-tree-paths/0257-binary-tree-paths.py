# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if not root:
            return []
        
        from collections import deque
        queue = deque([])
        queue.append((root, str(root.val)))

        res = []

        while queue:
            node, val = queue.popleft()
            if node.left:
                queue.append((node.left, f"{val}->{node.left.val}"))
            if node.right:
                queue.append((node.right, f"{val}->{node.right.val}"))

        
            if not node.left and not node.right:
                res.append(val)

        return res