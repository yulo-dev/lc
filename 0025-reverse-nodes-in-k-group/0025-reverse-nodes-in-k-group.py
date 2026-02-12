# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #類似lc92 頭插法的寫法
       
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            # 1) 跟lc92有點不同, 因為他要先走K步 確認這組夠長才可以反轉, 所以這邊會走到right boundary
            # 找到這組的第 k 個（kth）
            kth = prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # 不足 k 個就停, 回傳結果, 這邊也是最後跳出while loop的地方

            # 2) prev.next 是這組的頭（curr）
            # prev：指在「這一組前一個節點」
            # 所以 這一組的第一個節點 一定是 prev.next
            curr = prev.next

            # 3) 做 k-1 次頭插：把 curr.next 搬到 prev 後面
            for _ in range(k - 1):
                nxt = curr.next
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt

            # 4) curr 反轉後變成尾巴；把 prev 移到尾巴，準備下一組
            # curr 一開始是這組的頭（prev.next）
            #你做了 k-1 次頭插，把後面的節點一個個搬到前面
            #結果：這組反轉後，原本的頭 curr 會變成這組的尾巴
            prev = curr