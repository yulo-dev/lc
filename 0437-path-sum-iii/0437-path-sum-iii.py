# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        res = 0
        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_sum += node.val

            nonlocal res
            res += prefix_count.get(curr_sum - targetSum, 0)

            prefix_count [curr_sum] += 1

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            prefix_count [curr_sum] -= 1

            return res

        dfs(root, 0)

        return res