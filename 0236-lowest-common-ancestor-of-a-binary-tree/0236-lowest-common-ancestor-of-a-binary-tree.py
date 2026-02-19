# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # 1. 終止條件：撞牆了，或者是找到了其中一人
        # 如果我（目前的節點）就是我們要找的 $p$ 或 $q$，那我不必再往下看了，直接跟爸爸回報我找到了！
        # 不用往下找的原因是：就算 q 真的在 p 的下面，根據 LCA 的定義，p 本身就是 p 和 q 的祖先
        # 所以，只要遇到其中一個，就把自己當作「訊號」回傳給上一層
        if not root or root == p or root == q:
            return root
        
        # 2. 派人去左邊和右邊找 (Post-order)
        # 這邊的left or right 會回傳的有三種可能：
            # None -> 整個子樹都沒看到p 也沒看到q
            # p or q -> 如果在某個子樹中遇到p or q
            # 某個ancestor -> 找到某LCA 把它回傳
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        

        # 根據上面拿到的信號
        # 會有下面兩種情況的判斷
            # 左右都有信號：回傳自己是LCA
            # 只有一邊有信號：就把抓到的那一邊回傳

        # 3. 處理回報結果
        if left and right:
            # 兩邊都找到了，我就是那個祖先
            return root
        
        # 如果只有一邊有，就回報那一邊看到的結果（可能是 p, q 或者是已經找到的 LCA）
        return left if left else right


#這題不能比大小 因為不是BST
#只能去左右子樹看有沒有p or q
#如果兩邊都有人回報 代表目前的位子本身 就是LCA
#如果只有一邊回報 代表p,q在同一邊 那回報回來的結果就是LCA
#都沒人回報：代表這棵樹沒人