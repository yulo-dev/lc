# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        while curr and curr.next:
            #如果下一顆跟它一樣，就刪掉下一顆 但curr先不動
            if curr.val == curr.next.val:
                curr.next = curr.next.next

            #直到下一顆不同了，才代表這個值清完了，curr 才能往前走
            else:
                curr = curr.next

        return head