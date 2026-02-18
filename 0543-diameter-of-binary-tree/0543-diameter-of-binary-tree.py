# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_height = 0
        self.getHeight(root)
        return self.max_height
        
    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        
        self.max_height = max(self.max_height, left + right)

        return max(left, right) + 1