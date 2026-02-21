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
                #在 Python 的 heapq 裡存入 (node.val, node) 時，如果兩個 node.val 一樣，
                #Python 會試圖去比較 node 物件的大小，但 ListNode 是不能比較的，這會導致報錯。
                #解決方法：在 Tuple 中加入一個唯一的編號 i，變成 (node.val, i, node)。
                #這樣如果數值一樣，它會去比 i，就不會報錯
                heapq.heappush(h, (node.val, id(node), node))
        
        dummy = ListNode(0)
        tail = dummy

        while h:
            _, _, node = heapq.heappop(h)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(h, (node.next.val, id(node.next), node.next))

        return dummy.next


#想像你有 k 條已經排好序的隊伍（Linked Lists），每條隊伍的人都由矮到高排列。你要把他們合併成一條大隊伍。
#直覺作法：每次都看這 k 條隊伍的最前面那個人，選出最矮的那個。
#為什麼要用 Heap？：如果你有 100 條隊伍，每次都要用 for 迴圈看 100 個頭部節點來找最小值，太慢了O(k)。
#如果我們把這 k 個頭部節點丟進 Min-Heap，找最小值的時間就縮短成 O(logk)。

#algo:
    #初始化：把每一條非空的 Linked List 的 第一個節點 (head) 通通丟進 Min-Heap
    #從 Heap 中 heappop 出最小的節點。這就是我們合併後的下一個節點
    #如果這個被彈出的節點還有「下一個節點 (node.next)」，立刻把它的下一個節點再丟進 Heap
    #重複：直到 Heap 空了，合併也就完成了