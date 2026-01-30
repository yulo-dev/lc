# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        return self.merge_range(lists, 0, len(lists) - 1)

    def merge_range(self, lists, l, r):
        if l == r:
            return lists[l]

        mid = (l + r) // 2
        left = self.merge_range(lists, l, mid)
        right = self.merge_range(lists, mid + 1, r)
        return self.merge_two(left, right)

    def merge_two(self, a, b):
        dummy = ListNode(0)
        tail = dummy

        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        
        tail.next = a if a else b
        
        return dummy.next