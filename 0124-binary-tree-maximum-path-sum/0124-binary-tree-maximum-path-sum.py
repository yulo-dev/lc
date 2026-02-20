# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 1. 初始化全域最大值為無限小
        self.max_sum = float('-inf')

        def get_gain(node):
            if not node:
                return 0
            
            # 2. 遞迴計算左右子樹能提供的最大貢獻
            # 如果小孩貢獻是負數，我們就不要了 (取 0)，這是貪婪思想
            # 如果某個子樹的貢獻是負的，那包含它只會讓總和變小，所以我們寧願斷開連接，不取那一部分
            # 是總收益 不是單一個node是負的就斷開
            left_gain = max(get_gain(node.left), 0)
            right_gain = max(get_gain(node.right), 0)
            
            # 3. 【在地結算】第一步：算這條路徑如果「到我為止」有多少錢？
            # 試試看以目前節點為「轉折點」的路徑（左 + 我 + 右）
            # 這條路徑已經完整了，不能往上傳，只能用來挑戰紀錄
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # 4. 【對上貢獻】第二步：算如果我要「繼續往上走」有多少錢？
            # 回傳給爸爸：我 + (左或右比較大的那一邊)
            # 因為路徑不能分叉，傳上去的只能是一條直線
            return node.val + max(left_gain, right_gain)

        get_gain(root)
        return self.max_sum