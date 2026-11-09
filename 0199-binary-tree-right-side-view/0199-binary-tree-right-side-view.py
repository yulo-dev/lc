# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        from collections import deque
        
        queue = deque([])
        queue.append(root)
        res = []

        while queue:
            sz = len(queue)
            for i in range(sz):
                node = queue.popleft()
                if i == sz-1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
            