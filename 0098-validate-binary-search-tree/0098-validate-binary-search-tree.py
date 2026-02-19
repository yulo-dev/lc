# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        self.is_bst = True
        self.inorder(root)
        return self.is_bst

    def inorder(self, node):
        if not node or not self.is_bst:
            return

        self.inorder(node.left)

        if node.val <= self.prev:
            self.is_bst = False
            return

        self.prev = node.val

        self.inorder(node.right)