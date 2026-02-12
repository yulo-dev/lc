# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        #只要 head 可能會被改掉，就加 dummy
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next


        # 1 -> 2 -> 3 -> 4 -> 5
        # dummy - > 1 ->  2 ------> 3 -> 4 -> 5
        #           |     |              | 
        #          prev  left(curr)     right


        # (1) nxt = curr.next
        #
        # dummy - > 1 ->  2 --------> 3 ------> 4 -> 5
        #           |     |           |         | 
        #          prev  left(curr)  nxt      right


        # (2) curr.next = nxt.next  [curr跳過nxt 直接接到nxt.next]
        #
        #                 ---------(2)---------->
        #                 |                     |
        # dummy - > 1 ->  2 --------> 3 ------> 4 -> 5
        #           |     |           |         | 
        #          prev  left(curr)  nxt      right




        # (3) nxt.next = prev.next  [nxt轉指針 指向prev的下一個 就是curr]
        #
        #                 ---------(2)---------->
        #                 |                     |
        # dummy - > 1 ->  2           3 ------> 4 -> 5
        #           |     |           |         | 
        #                 <-----(3)----
        #          prev  left(curr)  nxt      right


        # (4) prev.next = nxt  [prev 指向nxt]
        #
        #            -------(4)------->
        #           ｜                ｜ 
        #           ｜                ｜    
        #           ｜     ---------(2)---------->
        #           ｜     |          ｜         |
        # dummy - > 1 ->  2           3 ------> 4 -> 5
        #           |     |           |         | 
        #                 <-----(3)----
        #          prev  left(curr)  nxt      right



        # dummy -> 1 -> 3 -> 2 -> 4 -> 5