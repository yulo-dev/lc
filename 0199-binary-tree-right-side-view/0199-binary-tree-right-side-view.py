# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        res = []

        def dfs(node, i):
            if not node:
                return
            
            if i == len(res):
                res.append(node.val)
            
            if node.right:
                dfs(node.right, i+1)
            
            if node.left:
                dfs(node.left, i+1)

        dfs(root, 0)

        return res


            