# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        #length + move to tail:
        length = 1
        curr = head
        while curr.next:  #為了避免curr走到None 這樣之後沒辦法直接接說 curr.next = head 去做cycle
            curr = curr.next
            length += 1

        #count rotate
        k = k % length
        if k == 0:
            return head

        #make a cycle
        curr.next = head

        #new tail & new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        #break cycle
        new_tail.next = None

        return new_head