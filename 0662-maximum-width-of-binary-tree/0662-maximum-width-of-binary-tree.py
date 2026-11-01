# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        
        from collections import deque

        if not root:
            return 0

        queue = deque()
        queue.append((root,1))

        res = 0

        while queue:
            sz = len(queue)
            min_order = float("inf")
            max_order = float("-inf")
            for _ in range(sz):
                node, idx = queue.popleft()

                min_order = min(min_order, idx)
                max_order = max(max_order, idx)
                
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))

            res = max(res, (max_order - min_order + 1))
            
        return res