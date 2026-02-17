# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base Case: 沒人可換就回傳
        if not root:
            return None

        # 2. 當前層邏輯: 直接交換左右指標
        root.left, root.right = root.right, root.left

        # 3. 交辦任務: 叫左邊跟右邊去處理它們自己的子樹
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
