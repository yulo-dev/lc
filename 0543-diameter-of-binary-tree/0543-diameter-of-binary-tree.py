# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1. 準備一個「全域筆記本」來紀錄最大直徑
        self.max_diameter = 0
        
        # 2. 啟動高度計算 (它會順便更新筆記本)
        self.getHeight(root)
        
        # 3. 最後回傳筆記本裡的最高紀錄
        return self.max_diameter

    def getHeight(self, node: Optional[TreeNode]) -> int:
        # Base case: 空節點高度為 0
        if not node:
            return 0
        
        # 遞迴拿到左右子樹的高度
        left_h = self.getHeight(node.left)
        right_h = self.getHeight(node.right)

        # 【核心動作】：經過我這個點的最長路徑就是 左高 + 右高
        # 我們把它跟筆記本裡的紀錄比比看，誰大就留誰
        self.max_diameter = max(self.max_diameter, left_h + right_h)

        # 【維持傳統】：還是要回傳「高度」給上司看
        return max(left_h, right_h) + 1