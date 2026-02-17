# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        # Queue 存的是 (當前節點, 從 Root 到這裡的累積總和)
        queue = deque([(root, root.val)])

        while queue:
            node, curr_sum = queue.popleft()

            # 判斷是否為葉子節點且總和達標
            # 根據題目的要求，路徑必須是 "root-to-leaf"（從根到葉子）
            # 在二元樹的結構中，一個節點如果既沒有左小孩，也沒有右小孩，它就是這條路徑的盡頭 
            # 所以這個if條件可以確保 只有在真的走到路盡頭時，才會去結算總和。
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True

            # 往下擴散，並更新下一層的累積和
            if node.left:
                queue.append((node.left, curr_sum + node.left.val))
            if node.right:
                queue.append((node.right, curr_sum + node.right.val))

        return False