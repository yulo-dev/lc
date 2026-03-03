# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        return self.inorder(root)

    def inorder(self, node):
        if not node:
            return True


        # 他會回傳boolean
        # 所以如果 self.inOrder(node.left) 的結果不是 True, 也就是左子樹驗證失敗了，那現在整棵樹也直接失敗，回傳 False。
        if not self.inorder(node.left):
            return False

        if node.val <= self.prev:
            return False

        self.prev = node.val

        return self.inorder(node.right)