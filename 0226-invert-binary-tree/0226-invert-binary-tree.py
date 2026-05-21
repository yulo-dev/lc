# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


#這題 preorder 跟 postorder 都能用，但 inorder 不行。
#Preorder（先交換再遞迴）： 交換左右 → 遞迴左 → 遞迴右 
#Postorder（先遞迴再交換）： 遞迴左 → 遞迴右 → 交換左右 
#Inorder（遞迴左 → 交換 → 遞迴右）： 左邊反轉完後交換到右邊，又被反轉一次 