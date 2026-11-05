# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.parent = {}

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.traverse(root, None)

        queue = deque()
        queue.append(target)
        
        visited = set()
        visited.add(target.val)

        dist = 0
        res = []

        while queue:
            sz = len(queue)
            for i in range(sz):
                node = queue.popleft()
                if dist == k:
                    res.append(node.val)

                parentNode = self.parent.get(node.val)
                if parentNode and parentNode.val not in visited:
                    queue.append(parentNode)
                    visited.add(parentNode.val) 
                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                    visited.add(node.left.val) 
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                    visited.add(node.right.val) 
            dist += 1
        return res
        
    def traverse(self, root, parentNode):
        if not root:
            return None

        self.parent[root.val] = parentNode
        self.traverse(root.left, root)
        self.traverse(root.right, root)