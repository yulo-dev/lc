# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # 1. 準備一個全域變數，紀錄「上一個看到的數字」
        # 一開始設為極小值
        # 為了確保整棵樹最左下角的那個「最小節點」可以順利通過第一次檢查
        self.prev = -float('inf')
        
        return self.inOrder(root)

    def inOrder(self, node):
        if not node:
            return True
        
        # --- 步驟 1: 先鑽到左邊最底 ---
        if not self.inOrder(node.left):
            return False
        
        # --- 步驟 2: 處理當前節點 (這是中序遍歷發生的點) ---
        # 如果當前的值「沒有」大於前一個值，代表這不是 BST
        # 因為 BST 的定義通常是「左子樹的所有值都小於當前值」，不能等於。如果有兩個點數值一樣（例如兩個 5），那就不是嚴格遞增，這就違反了 BST 的規定
        if node.val <= self.prev:
            return False
        
        # 更新「上一個數字」為目前的數字，準備給下一個點比對
        self.prev = node.val
        
        # --- 步驟 3: 鑽向右邊 ---
        return self.inOrder(node.right)