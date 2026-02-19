# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 如果名單空了，代表這條路走到底了，返回 None
        if not preorder or not inorder:
            return None

        # 1. Preorder 的第一個數字就是目前的 Root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 2. 在 Inorder 裡找到 Root 的位置，這就是左右子樹的分水嶺
        # 假設 mid = 2，代表左子樹有 2 個節點
        # index是尋找某個元素在列表中的索引位置
        mid = inorder.index(root_val)

        # 3. 遞迴蓋房子
        # 左子樹：
        # Preorder 扣掉第一個 root 後，拿接下來的 mid 個
        # Inorder 拿 mid 之前的
        # 重點在於 不管是前序還是中序，左子樹的節點數量永遠是一樣的, 所以inorder算出來的mid可以拿來切preorder
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        # 右子樹：
        # Preorder 拿 mid+1 之後剩下的所有
        # Inorder 拿 mid+1 之後的所有
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root

    
    