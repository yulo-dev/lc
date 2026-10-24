# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while curr1 or curr2 or carry:

            v1 = curr1.val if curr1 else 0 
            v2 = curr2.val if curr2 else 0 

            tot = v1 + v2 + carry
            digit = tot % 10
            carry = tot // 10

            curr.next = ListNode(digit)
            curr = curr.next

            if curr1:
                curr1 = curr1.next
            
            if curr2:
                curr2 = curr2.next

        return dummy.next