# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        
        ordering = []
        self.inorder(root, ordering)

        return ordering[k-1]


    def inorder(self, root, ordering):
        if not root:
            return None
        self.inorder(root.left, ordering)
        ordering.append(root.val)
        self.inorder(root.right, ordering)