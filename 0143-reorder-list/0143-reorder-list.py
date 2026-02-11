# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1) find middle (slow will end at mid)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is mid, split into two lists: head..slow and slow.next..end
        second = slow.next
        slow.next = None  # cut

        # 2) reverse second half
        curr = second
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev  # 把 second 的頭指回正確的新頭

        # 3) merge (weave) first and second
        first = head
        while second:
            # save next pointers
            t1 = first.next # 先存 first 的下一個（不存會丟掉）
            t2 = second.next # 先存 second 的下一個（不存會丟掉）

            # weave one node from second into first
            first.next = second # 把 second 插到 first 後面
            second.next = t1 # 再把 second 接回原本 first 後面的節點

            # move forward
            first = t1  # first 往前（走到下一個要接的位置）
            second = t2  # second 往前（走到下一個要插的節點）



#理解第三part 交叉merge:
#舉例:
#first: 1 -> 2 -> 3 
#second: 5 -> 4
#first=1, second=5

#第一輪
#t1 = first.next = 2
#t2 = second.next = 4

#first.next = second → 1.next = 5
#second.next = t1 → 5.next = 2

#first = t1 → first = 2 
#second = t2 → second = 4
#此時鏈變成：1 -> 5 -> 2 -> 3

#第二輪
#t1 = first.next = 3
#t2 = second.next = None

#first.next = second → 3.next = 4
#second.next = t1 → 4.next = 3

#first = t1 → first = 3 
#second = t2 → second = None
#此時鏈變成：1 -> 5 -> 2 -> 4 -> 3