# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 如果最終高度不是 -1，代表整棵樹都平衡
        return self.getHeight(root) != -1

    def getHeight(self, node: Optional[TreeNode]) -> int:
        # 1. Base Case: 空節點高度為 0
        if not node:
            return 0

        # 2. 探查左邊 (左邊請回報高度)
        left_height = self.getHeight(node.left)
        # 這代表左邊那棵子樹裡，已經有某兩個點的高度差超過 1 了，直接向上傳遞
        if left_height == -1:
            return -1

        # 3. 探查右邊 (右邊請回報高度)
        right_height = self.getHeight(node.right)
        # 這代表右邊那棵子樹裡，已經有某兩個點的高度差超過 1 了，直接向上傳遞
        if right_height == -1:
            return -1

        # 4. 當前層判斷: 檢查我有沒有出問題
        if abs(left_height - right_height) > 1:
            return -1

        # 5. 沒問題的話，回傳我正常的高度
        return max(left_height, right_height) + 1
    