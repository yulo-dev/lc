# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 1. 如果樹是空的，直接失敗
        # 根據題目的定義，一條「路徑（Path）」必須從 根節點 (Root) 開始，到 葉子節點 (Leaf) 結束。
        # 如果樹是空的，代表它連一個節點都沒有 -> 沒有節點，就代表不存在任何路徑 -> 既然連路徑都沒有，自然不可能有一條總和為 0 的路徑
        if not root:
            return False

        # 2. 如果是葉子節點，檢查剩下的錢夠不夠付
        if not root.left and not root.right:
            return targetSum == root.val

        # 3. 如果不是葉子，扣掉自己的值，叫小孩去湊剩下的
        # 只要左邊「或」右邊有一條路通，就是 True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
