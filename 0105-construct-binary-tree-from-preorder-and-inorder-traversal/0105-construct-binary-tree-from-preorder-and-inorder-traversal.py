# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        
        def build(preorder, inorder):
            if not preorder:
                return None
            
            root = TreeNode(preorder[0])
            root_index = inorder.index(preorder[0])

            root.left = build(
                            preorder[1:root_index+1], inorder[0:root_index]
                            )

            root.right = build(
                            preorder[root_index+1:], inorder[root_index+1:]
                            )

            return root

        return build(preorder, inorder)