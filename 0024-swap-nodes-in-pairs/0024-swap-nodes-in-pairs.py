# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next

            curr.next = second
            first.next = second.next
            second.next = first

            curr = first
        
        return dummy.next