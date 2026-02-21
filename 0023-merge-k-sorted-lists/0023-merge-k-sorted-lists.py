# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            new_list = []     
            
            #for loop這邊先負責把「能成對的」通通抓去合併
                             #為了正常抓到i+1, 這邊記得-1
            for i in range(0, len(lists) - 1, 2):
                merged = self.merge_two(lists[i], lists[i+1])
                new_list.append(merged)

            #這個if 負責把那個「因為減 1 而被迴圈遺忘的落單者」抓回來放進 new_list
            if len(lists) % 2 == 1:
                new_list.append(lists[-1])
            
            #狀態更新 這樣最外層的while loop才能正確的停下
            lists = new_list

        return lists[0]

    # 這裡就是最基本的 LC 21 合併兩條有序鏈結串列的邏輯
    def merge_two(self, a, b):

        dummy = ListNode(0)
        tail = dummy

        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        
        tail.next = a if a else b
        
        return dummy.next
            