# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # 把 k 存進 self，這樣所有層級的遞迴都能看到同一個 k
        self.k = k
        self.res = None
        
        self.inorder(root)
        return self.res
        
    def inorder(self, node):

        # 1. 如果已經找到答案，或者走到空節點，就不用再跑了
        if not node or self.res is not None:
            return

        # 2. 往左走 (最左邊最小)
        self.inorder(node.left)

        # 3. 中間處理 (點名)
        self.k -= 1 # 看到一個人，k 就減 1
        if self.k == 0:
            self.res = node.val
            return # 找到了！
        
        # 4. 往右走
        self.inorder(node.right)