# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        queue = deque([root])
        res = []
        while queue:
            level_len = len(queue) #這邊要先存出一個邊數
            for i in range(len(queue)):
                node = queue.popleft()
                if i == level_len - 1: #給這邊使用, 不能直接 i == len(queue) 因為queue會一直變動
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res

