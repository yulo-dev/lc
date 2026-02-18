# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 輔助函數：負責處理特定範圍內的數字
        def build(left, right):
            # 終止條件：如果左邊超過右邊，代表沒數字了
            if left > right:
                return None
            
            # 找到中間點的 index
            mid = left + (right - left) // 2
            
            # 1. 創立當前區間的老大
            node = TreeNode(nums[mid])
            
            # 2. 遞迴蓋左邊 (範圍變成 left 到 mid-1)
            node.left = build(left, mid - 1)
            
            # 3. 遞迴蓋右邊 (範圍變成 mid+1 到 right)
            node.right = build(mid + 1, right)
            
            return node
            
        return build(0, len(nums) - 1)

    