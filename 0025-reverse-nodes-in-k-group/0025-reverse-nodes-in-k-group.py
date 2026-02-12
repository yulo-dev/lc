# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
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
            old_head = prev.next            # 反轉前的頭 -> 反轉後的尾巴
            old_head.next = next_start      # 尾巴接回下一段
            prev.next = new_head            # groupPrev 接到新頭
            prev = old_head                 # prev 移到尾巴，準備下一組
            

    def reverse_linked_list(self, head, k):
        previous, current, nxt = None, head, None
        for _ in range(k):
            nxt = current.next # temporarily store the nxt node
            current.next = previous # reverse the current node
            previous = current # before we move to the next node, point previous to the current node
            current = nxt  # move to the nxt node 
        return previous, current