# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # 一直兩兩合併，直到剩一條
        while len(lists) > 1:
            new_lists = []

            # 每次取兩條 merge
            for i in range(0, len(lists) - 1, 2):
                merged = self.merge_two(lists[i], lists[i + 1])
                new_lists.append(merged)

            # 如果是奇數條，最後一條直接帶到下一輪
            if len(lists) % 2 == 1:
                new_lists.append(lists[-1])

            lists = new_lists

        return lists[0]

    def merge_two(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        # 把剩下那條直接接上
        tail.next = a if a else b
        return dummy.next