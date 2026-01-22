# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less_dummy = ListNode()
        less = less_dummy

        ge_dummy = ListNode()
        ge = ge_dummy

        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                ge.next = curr
                ge = ge.next

            curr = curr.next

        ge.next = None
        less.next = ge_dummy.next # 因為ge_dummy是假頭 要接ge_dummy 的第一個真正的節點

        return less_dummy.next

        