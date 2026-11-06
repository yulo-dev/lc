# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.parent = {}

    def traverse(self, root, parentNode):
        if not root:
            return None
        self.parent[root.val] = parentNode
        self.traverse(root.left, root)
        self.traverse(root.right, root)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.traverse(root, None)
        dist = 0

        queue = deque()
        queue.append(target)

        visited = set()
        visited.add(target.val)

        res = []

        while queue:
            sz = len(queue)
            for _ in range(sz):
                node = queue.popleft()
                if dist == k:
                    res.append(node.val)
                
                parentNode = self.parent.get(node.val)
                if parentNode and parentNode.val not in visited:
                    visited.add(parentNode.val)
                    queue.append(parentNode)

                if node.left and node.left.val not in visited:
                    visited.add(node.left.val)
                    queue.append(node.left)

                if node.right and node.right.val not in visited:
                    visited.add(node.right.val)
                    queue.append(node.right)

            dist += 1

        return res