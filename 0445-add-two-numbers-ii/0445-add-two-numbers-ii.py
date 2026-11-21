# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        head = None
        carry = 0

        stack1 = []
        stack2 = []

        self.push_stack(l1, stack1)
        self.push_stack(l2, stack2)

        while stack1 or stack2 or carry:
            l1_val = stack1.pop() if stack1 else 0
            l2_val = stack2.pop() if stack2 else 0

            tot = l1_val + l2_val + carry

            carry = tot // 10
            digit = tot % 10

            new_node = ListNode(digit)
            new_node.next = head
            head = new_node

        return head


    def push_stack(self, head, stack):
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next