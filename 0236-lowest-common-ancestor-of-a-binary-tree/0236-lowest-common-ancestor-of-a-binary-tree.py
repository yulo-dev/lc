# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


#My approach is to use DFS recursion.
#For each node, I recursively search the left and right subtrees.
#The key idea is that the recursive call returns whether it found p, q, or the LCA candidate in that subtree.

#There are three important cases:
    #If the current node is None, I return None.
    #If the current node is p or q, I return the current node.
    #After searching left and right, if both sides return non-null, that means p and q are found in different subtrees, so the current node is their lowest common ancestor.