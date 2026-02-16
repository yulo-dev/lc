# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. 終止條件：處理 None 的情況 
        if not p and not q: 
            return True   # 兩邊都空，相等
        if not p or not q: 
            return False    # 一邊空一邊有，不相等

        # 2. 當前層檢查：值不一樣就不用往下比了
        if p.val != q.val: return False

        # 3. 交辦任務：左邊一樣 且 右邊一樣
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))