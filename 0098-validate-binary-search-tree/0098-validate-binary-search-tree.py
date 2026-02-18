# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, node, low, high):
        if not node:
            return True
        
        # 核心檢查：當前值必須在 (low, high) 區間內
        if not (low < node.val < high):
            return False
        
        # 往左走：上限更新為當前值 (high = node.val)
        # 往右走：下限更新為當前值 (low = node.val)
        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, high)