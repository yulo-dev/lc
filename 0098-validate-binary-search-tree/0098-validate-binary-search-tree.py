# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        res = []
        self.inorder(root, res)

        for i in range(len(res)):
            if i > 0 and res[i] <= res[i-1]:
                return False

        return True

    def inorder(self, root, res):
        if not root:
            return 
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)