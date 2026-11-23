# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root)
        return self.maxDiameter

    def maxDepth(self, root):
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        curr_diameter = left_depth + right_depth

        #因为要在 maxDepth 的后序位置操作外部变量，题目最终要的答案是那个外部变量，而不是 maxDepth 的返回值。
        #所以这种情况下只能新建一个函数。如果题目要的答案恰好是你函数的返回值，那么你才可以直接用原函数递归
        self.maxDiameter = max(self.maxDiameter, curr_diameter)

        return 1 + max(left_depth, right_depth)