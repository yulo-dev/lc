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
        
        # 1) pre 走到 left 前一個（第 left-1 個）
        # 要記得起點是dummy 所以會多走一步, dummy是第0個node, head是第一個node
        # linked list 的「第幾個節點」這種說法常用 1-based（第 1 個就是 head），但 array index 通常是 0-based
        for _ in range(left - 1):
            prev = prev.next

        # 2) cur 是 left 位置（反轉區間的第一個）
        cur = prev.next

        # 3) 反轉 right-left 次：每次把 cur.next 抽出來插到 prev 後面
        for _ in range(right - left):
            move = cur.next          # 取出 curr 後面那個節點（等下要把它「搬到 prev 後面」當成新頭）
            cur.next = move.next     # 把 move 從原本位置拔掉：讓 curr 直接跳過 move，接到 move 的下一個
            move.next = prev.next     # 讓 move 指向原本 pre 後面的東西
            prev.next = move          # 讓 pre 指向 move

        return dummy.next