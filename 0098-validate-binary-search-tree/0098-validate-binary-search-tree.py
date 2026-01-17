# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, left, right):
            if not node:
                return True

            if not (left < node.val < right): # 這個節點違規，整棵樹直接不合法
                return False

            # 檢查是不是「整棵樹」都通過
            return (validate(node.left, left, node.val) and validate(node.right, node.val, right))

        return validate(root, float("-inf"), float("inf"))