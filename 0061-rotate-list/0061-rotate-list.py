# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head
        
        # (1) find length n and tail
        length = 1
        curr = head

        while curr.next:
            curr = curr.next
            length += 1
        
        # (2) 計算需要rotate幾次, 因為如果rotate n次會回到原狀
        k = k % length
        if k == 0:
            return head

        # (3) make it a cycle
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        curr.next = head

        # (4) Find new tail: (n - k) steps from head to reach new head,
        # so new tail is (n - k - 1) steps from head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next

        # 5) Break the cycle
        new_tail.next = None

        return new_head