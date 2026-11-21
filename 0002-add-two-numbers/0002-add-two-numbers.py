# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        dummy = ListNode()
        head = dummy

        l1_curr = l1
        l2_curr = l2
        carry = 0

        while l1_curr or l2_curr or carry:
            l1_val = l1_curr.val if l1_curr else 0
            l2_val = l2_curr.val if l2_curr else 0

            tot = l1_val + l2_val + carry

            carry = tot // 10
            digit = tot % 10

            head.next = ListNode(digit)
            head = head.next

            if l1_curr:
                l1_curr = l1_curr.next 
            if l2_curr:
                l2_curr = l2_curr.next

        return dummy.next
            


