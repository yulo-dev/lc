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

    def merge_range(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left + right) // 2

        left_list = self.merge_range(lists, left, mid)
        right_list = self.merge_range(lists, mid+1, right)

        return self.merge_two(left_list, right_list)


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
