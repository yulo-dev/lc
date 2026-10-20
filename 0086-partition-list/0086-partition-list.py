# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        less = dummy1
        greater = dummy2

        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        greater.next = None
        less.next = dummy2.next

        return dummy1.next