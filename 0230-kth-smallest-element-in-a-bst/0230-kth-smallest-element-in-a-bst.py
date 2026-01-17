# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0

        def inorder(node):
            if not node:
                return 

            left = inorder(node.left)
            if left != None:
                return left
            
            self.cnt += 1

            if self.cnt == k:
                return node.val

            return inorder(node.right)

        return inorder(root)
            