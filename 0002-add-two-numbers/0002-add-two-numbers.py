# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 

            tot = v1 + v2 + carry
            digit = tot % 10
            carry = tot // 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

        return dummy.next