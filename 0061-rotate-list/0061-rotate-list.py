# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        
        #k divided by the length of list and the remainer = the time to rotate
        #how to get the length:
            #use for loop to iterate through the linkedlist
        #how to rotate:
            #two pointers: one pointer will move to the kth position from the end (linkedlist A), the other remain from the start (linkedlist B)
            #link the end of linkedlist A.next = head of linkedlist B 

        if not head:
            return None
        
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        new_k = k % length

        if new_k == 0:
            return head


        # find new tail / old tail

        slow = fast = head

        for _ in range(new_k):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # reconnect
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head