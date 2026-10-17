# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #cut into 2 parts: slow/fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #reverse the 2nd part
        prev = None
        curr = slow.next

        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #merge the 2 lists
        first = head
        second = prev

        while first and second:
            remain_first = first.next
            first.next = second
            first = remain_first

            remain_second = second.next
            second.next = first
            second = remain_second

        if second:
            first.next = second

        return head
            