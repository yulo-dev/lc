# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # 一開始就先往左衝到底，把路上的節點都存起來
        self._push_left(root)


    # 這是為了找最小的
    # 在 BST 中，只要一個節點有 「左小孩」，它就不可能是最小的。所以，當你拿到一個點，你必須一路向左鑽到底，直到撞牆為止
    # Stack 最上面的那個，就是這條路徑上的「最左邊」，也就是當前的最小值
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left # 一直往左

    def next(self) -> int:
        # 彈出的就是目前最小的
        node = self.stack.pop()
        
        # 如果它有右邊，就要把右邊那棵子樹的「左側牆壁」也加進來
        if node.right:
            self._push_left(node.right)
            
        return node.val
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0



#To implement the BST Iterator, my goal is to perform an in-order traversal (Left-Root-Right) to ensure the values are returned in ascending
#order. However, instead of using a recursive approach that would require $O(N)$ space to store all nodes upfront, I will use a Stack to #simulate the recursion manually. This allows us to achieve a more efficient O(H) space complexity, where H is the height of the tree.

#The core of my approach is a helper function, let’s call it _push_left.
#Initialization: In the constructor, I immediately call _push_left on the root. 
#This pushes the root and all its left descendants onto the stack.
#in a BST, the smallest element is always the 'left-most' node. By the end of this step, the smallest element is at the top of my stack.


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()