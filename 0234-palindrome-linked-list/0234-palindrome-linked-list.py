# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse
        prev = None
        curr2 = slow

        while curr2:
            nxt = curr2.next
            curr2.next = prev
            prev = curr2
            curr2 = nxt
        
        #compare
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next
        
        return True