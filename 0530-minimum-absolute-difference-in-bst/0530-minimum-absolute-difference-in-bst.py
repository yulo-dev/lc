# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = float("-inf")
        self.res = float("inf")

        self.inorder(root)

        return self.res 

    def inorder(self, node):
        if not node:
            return 
        
        self.inorder(node.left)

        self.res = min(self.res, node.val - self.prev)
        self.prev = node.val

        self.inorder(node.right)