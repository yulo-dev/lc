# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        #需要 prev 的原因是：當你發現一段重複值時，你要把「整段」從鏈上剪掉，必須修改的是“重複段前一個節點”的 .next。
        #這個「前一個節點」就是 prev
        prev = dummy

        #curr 是往前走、判斷現在這段是不是 duplicates，並跳過整段重複
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val
                while curr and curr.val == dup_val:
                    curr = curr.next
                prev.next = curr #當跳出while loop 代表curr 是停在第一個不重複的node上 所以prev可以直接接上他 等於跳過中間重複的
            else:
                prev = curr
                curr = curr.next

        return dummy.next