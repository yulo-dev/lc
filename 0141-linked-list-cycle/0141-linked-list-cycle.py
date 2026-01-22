# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


            # If there is a cycle, fast will eventually catch up to slow inside the cycle, because it moves faster and keeps looping
            # Think of it like two runners on a track. If there’s a loop, the faster runner will lap the slower one.
            if slow == fast:
                return True

        return False