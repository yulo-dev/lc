# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
    
        def build(nums):
            if not nums:
                return None
            
            max_value = max(nums)

            #max_index = nums.index(max_value)
            for i in range(len(nums)):
                if nums[i] == max_value:
                    max_index = i

            root = TreeNode(max_value)
            root.left = build(nums[0:max_index])
            root.right = build(nums[max_index+1:len(nums)])

            return root

        return build(nums)