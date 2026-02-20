# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. 把樹變成有序陣列
        nums = []
        self.inorder_extract(root, nums)

        # 2. 把有序陣列變回平衡 BST (這就是 LC 108!)
        return self.build_balanced_tree(0, len(nums) - 1, nums)


    #step 1: 把散落在樹裡的數值，按照從小到大的順序，整齊地排進一個 Array (List) 裡
    #因為你原本的樹可能長得很「歪」（例如全部往右長，像個長條形），這在電腦科學裡叫 Skewed Tree。這種樹的搜尋效率很差
    #為了把它重新蓋成「平衡」的樣子，最簡單的方法就是： 全部拆掉 --> 重新蓋好
    def inorder_extract(self, node, nums):
        if not node: 
            return

        self.inorder_extract(node.left, nums)
        nums.append(node.val)
        self.inorder_extract(node.right, nums)
    
    #step 2: 重組（蓋平衡樹）(這就是 LC 108!)
    def build_balanced_tree(self, left, right, nums):
        #當一個node沒有child時 這行就會觸發
        if left > right:
            return None

        mid = left + (right - left) // 2
        node = TreeNode(nums[mid])

        node.left = self.build_balanced_tree(left, mid - 1, nums)
        node.right = self.build_balanced_tree(mid + 1, right, nums)

        return node