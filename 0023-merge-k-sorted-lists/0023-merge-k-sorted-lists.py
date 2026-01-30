# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        for node in lists:
            if node:
                #id(node) 是 Python 內建函式 id() 回傳的 物件身分識別值（通常可視為這個物件在記憶體中的唯一標識，
                #至少在它存活期間是唯一的）
                #你把 heap 元素放成 (node.val, id(node), node) 的原因是：
                #當 node.val 一樣時，heap 需要第二個欄位來打破平手（tie-breaker），否則 Python 會試著比較 node 本身。
                heapq.heappush(h, (node.val, id(node), node)) 
        
        dummy = ListNode(0)
        tail = dummy

        # 2) 反覆取最小，接到結果，再推入 next
        while h:
            _, _, node = heapq.heappop(h)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(h, (node.next.val, id(node.next), node.next))

        tail.next = None
        return dummy.next 