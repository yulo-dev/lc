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

        print("Enter:", root.val)

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        print("calculate:", root.val)

        # 1.計算經過目前 Node 的 Diameter
        curr_diameter = left_depth + right_depth

        # 2. 更新整棵 Tree 目前找到的最大 Diameter
        #The diameter doesn't necessarily pass through the root, 
        #so I need to consider every node as a potential turning point of the longest path.
        self.maxDiameter = max(self.maxDiameter, curr_diameter)

        return 1 + max(left_depth, right_depth)

      