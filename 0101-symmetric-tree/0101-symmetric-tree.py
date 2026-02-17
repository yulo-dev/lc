# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # 呼叫輔助函式，開始比對左子樹跟右子樹
        return self.isMirrow(root.left, root.right)

    def isMirrow(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Base Case: 處理 None
        if not p and not q:
            return True

        if not p or not q:
            return False

        # 2. 當前層邏輯: 值要一樣
        if p.val != q.val:
            return False

        # 3. 交辦任務: 核心鏡像邏輯
        # 比對 (p 的左 vs q 的右) AND (p 的右 vs q 的左)
        return (self.isMirrow(p.left, q.right) and self.isMirrow(p.right, q.left))