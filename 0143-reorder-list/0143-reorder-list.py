# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 找到中點 然後切成前後半
        curr = head
        slow = fast = curr

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
       
        # 反轉後半
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 合併
        first = head
        second = prev

        while first and second:
            nxt_first = first.next
            nxt_second = second.next

            first.next = second
            second.next = nxt_first
            
            first = nxt_first
            second = nxt_second


            
