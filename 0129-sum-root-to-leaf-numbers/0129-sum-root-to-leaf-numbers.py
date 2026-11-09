# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        total = 0

        def dfs(node, val):
            nonlocal total
            
            if not node.left and not node.right:
                total += val

            if node.left:
                dfs(node.left, val*10 + node.left.val)
            if node.right:
                dfs(node.right, val*10 + node.right.val)
            
        dfs(root, root.val)

        return total