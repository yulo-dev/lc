# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        dummy = ListNode(0)
        curr = dummy

        heap = []
        i = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, i, node))
                i += 1

        while heap:
            min_node_val, idx, min_node = heapq.heappop(heap)

            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, idx, min_node.next))

            curr.next = min_node
            curr = curr.next
            
        return dummy.next
