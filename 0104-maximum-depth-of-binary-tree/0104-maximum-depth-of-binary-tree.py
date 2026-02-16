# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        #我這層的高度，就是左右兩邊比較高的那個，再加 1（加上我這一層）
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))