# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        
        dummy = ListNode(0, head)
        start = dummy
        for _ in range(left-1):
            start = start.next
        tail = start.next

        end = head
        for _ in range(right):
            end = end.next

        prev = None
        curr = tail

        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            

        start.next = prev
        tail.next = end

        return dummy.next


        
        