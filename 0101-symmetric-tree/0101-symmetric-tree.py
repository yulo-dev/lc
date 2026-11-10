# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        
        queue = deque([])
        queue.append(root)

        while queue:
            sz = len(queue)
            level = []

            for _ in range(sz):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    level.append(node.left.val)
                if not node.left:
                    level.append('#')
                    
                if node.right:
                    queue.append(node.right)
                    level.append(node.right.val)
                if not node.right:
                    level.append('#')

            if level != level[::-1]:
                return False
        
        return True
                
