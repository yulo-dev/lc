# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return [] 
        
        from collections import deque
        
        queue = deque([])
        queue.append((root, root.val, [root.val]))
        res = []
        while queue:
            node, val, path = queue.popleft()

            if not node.left and not node.right and val == targetSum:
                res.append(path)

            if node.left:
                queue.append((node.left, val + node.left.val, path + [node.left.val]))
            if node.right:
                queue.append((node.right, val + node.right.val, path + [node.right.val]))

        return res