# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        
        queue = deque()
        queue.append((root,1))
        res = float("-inf")

        while queue:
            sz = len(queue)
            min_index = float("inf")
            max_index = float("-inf")
            for _ in range(sz):
                node, idx = queue.popleft()
                min_index = min(min_index, idx)
                max_index = max(max_index, idx)
                res = max(res, max_index - min_index + 1)

                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))

        return res


