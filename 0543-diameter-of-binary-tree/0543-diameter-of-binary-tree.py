# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightOfBinaryTree(self, root):
        if not root:
            return 0
        left_height = self.heightOfBinaryTree(root.left)
        right_height = self.heightOfBinaryTree(root.right)

        self.max_diameter = max(self.max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        self.heightOfBinaryTree(root)

        return self.max_diameter