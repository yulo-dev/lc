# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        if not root:
            return 0
        
        left_h = left_height(root)
        right_h = right_height(root)

        if left_h == right_h:
            return (1 << left_h) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)