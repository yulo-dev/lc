# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        def dfs(node, val):
            if not node.left and not node.right:
                return val

            total = 0

            if node.left:
                total += dfs(node.left, val*10 + node.left.val)
            if node.right:
                total += dfs(node.right, val*10 + node.right.val)
            
            return total

        return dfs(root, root.val)