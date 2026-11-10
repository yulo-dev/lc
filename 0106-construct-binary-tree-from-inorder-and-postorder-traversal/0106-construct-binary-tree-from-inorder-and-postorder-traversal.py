# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        
        def build(inorder, postorder):
            if not inorder:
                return None

            root = TreeNode(postorder[-1])
            root_index = inorder.index(postorder[-1])

            root.left = build(inorder[:root_index], postorder[:root_index])
            root.right = build(inorder[root_index+1:], postorder[root_index:len(postorder)-1])

            return root

        return build(inorder, postorder)