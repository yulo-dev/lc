# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        #count the total length of the linkedlist
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1

        #count the exact rotate time
        k = k % length
        if k == 0:
            return head

        #make it a cycle
        curr.next = head

        #find the new tail and then we can get the new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # find the new head (which is next to the new tail)
        new_head = new_tail.next
        
        # break the cycle
        new_tail.next = None

        return new_head