# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        #每一輪（每一組 k 個）你都要先鎖定這組的 三個位置：
            # A = prev：這組「前一個節點」
            # B = prev.next（也就是 old_head）：這組「第一個節點」（反轉開始點，反轉後會變尾巴）
            # C = kth：這組「第 k 個節點」（反轉後會變頭）
            # D = kth.next（也等於 next_start）：這組「後一個節點」（下一組的開始）

            #畫成一條線就是：
            #... -> A(prev) -> B(prev.next, 組頭) -> ... -> C(kth,組尾) -> D(kth.next) -> ...
            #要反轉的: 反轉 B 到 C 這段（剛好 k 個）。
        
        dummy = ListNode(0, head)
        prev = dummy
    
        while True:
            # 先確認剩下夠不夠 k 個：找到第 k 個
            kth = prev
            for _ in range(k):
                kth = kth.next
                if kth == None:
                    return dummy.next   # 直接結束
        
            # 反轉 k 個
            new_head, next_start = self.reverse_linked_list(prev.next, k)

            # 接回去
            old_head = prev.next         # 反轉前的頭 -> 反轉後的尾巴
            old_head.next = next_start   # B.next = D   (新尾巴接回後面)
            prev.next = new_head         # A.next = new_head(=C)  (前面接新頭)
            prev = old_head              # 移到下一組：A 變成這輪的尾巴


    def reverse_linked_list(self, head, k):
        prev, curr, nxt = None, head, None
        for _ in range(k):
            nxt = curr.next # temporarily store the nxt node
            curr.next = prev # reverse the current node
            prev = curr # before we move to the next node, point previous to the current node
            curr = nxt  # move to the nxt node 
        return prev, curr