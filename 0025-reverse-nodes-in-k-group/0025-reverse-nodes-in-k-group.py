# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        start = end = dummy

        while start:
            end = start

            #每k個一切
            for _ in range(k):
                end = end.next
                if not end:
                    return dummy.next

            #先存好必要資訊 之後要串在一起使用 (先保存這一組前後的連接點)
            group_next = end.next
            group_prev = start

            #再來反轉
            prev = group_next
            curr = start.next
            group_head = curr

            while curr and curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            #串
            #把前一段接到反轉後的新head
            group_prev.next = prev

            #原本的 group head 現在變成 tail
            #也就是下一組的 group_prev
            start = group_head
                
        return dummy.next