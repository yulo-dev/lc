# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #類似lc206 指標反轉的寫法 只是只反轉k個
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # 1) 找到這組的第 k 個（kth）
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # 不足 k 個就停, 回傳結果, 這邊也是最後跳出while loop的地方

            # 2)  after = 下一組的開頭（這組後面的那個）
            groupNext = kth.next

            # 3) 反轉這一組（用 LC206 的寫法，但只做 k 次）
            prev = groupNext
            curr = groupPrev.next    # 這組的頭
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 4) 接回去 + 移動 pre 到下一組
            # 反轉前的頭（groupPrev.next）反轉後會變這組的尾巴
            old_head = groupPrev.next
            groupPrev.next = prev     # prev 是反轉後的新頭
            groupPrev = old_head      # 下一輪從這組尾巴開始