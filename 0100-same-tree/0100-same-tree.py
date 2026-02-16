# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = deque([(p, q)])
        
        while queue:
            for _ in range(len(queue)):
                node1, node2 = queue.popleft()

                # 1. 如果兩邊都是空的 -> 沒問題，繼續看下一對
                if not node1 and not node2:
                    continue
                
                # 2. 如果一邊空一邊不空，或者值不一樣 -> 抓到不同，回傳 False
                if not node1 or not node2 or node1.val != node2.val:
                    return False

                # 3. 將左右子樹「成對」塞入。就算其中一個是 None 也要塞，
                # 這樣上面的 if not node1 or not node2 才會抓到不對稱。
                queue.append([node1.left, node2.left])
                queue.append([node1.right, node2.right])

        return True
                