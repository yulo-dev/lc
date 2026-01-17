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

            if left is not None:
                return left # 1) 左邊有答案就直接回傳

            # 2) 左邊沒答案，才處理自己
            self.cnt += 1
            
            if self.cnt == k:
                return node.val

            # 3) 自己也不是答案，才去右邊
            return inorder(node.right)

        return inorder(root)