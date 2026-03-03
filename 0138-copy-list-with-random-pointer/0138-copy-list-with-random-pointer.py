"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""




#為什麼不能直接一路複製:
    #因為如果只有 next，你可以一路往後建。
    #但這題還有 random：
    #假設目前在舊節點 A，它的 random -> C
    #你在複製 A 的時候，C 的新節點可能還沒建立好。
    #所以需要一個表去記：舊節點對應到哪個新節點
    #這就是 hashmap 的用途。


#Two Pass + Hashmap

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldtonew = {None: None}

        #Pass 1: 先把每個舊 node 對應的新 node 建好
        # 這時候只是做出：
            #A -> A'
            #B -> B'
            #C -> C'
        #但A'.next 還沒接
        #A'.random 還沒接
        #B'.next 也還沒接
        #所以新節點本身都存在了，但彼此關係還沒完整建立
        curr = head
        while curr:
            oldtonew[curr] = Node(curr.val)
            curr = curr.next

        #Pass 2: 再把新 node 的：next, random 接起來
        #因為第二輪時，所有新節點都已經存在 map 裡了，所以不管 random 指到前面、後面、自己、或 None，都能直接找到
        curr = head
        while curr:
            copy = oldtonew[curr]                       #找到「目前這個舊節點 curr」對應的「新節點 copy」
            copy.next = oldtonew[curr.next]             #把「新 curr」的 next，指向「舊 curr.next 對應的新 node」
                                                        #A'.next = B'
            copy.random = oldtonew[curr.random]         #把「新 curr」的 random，指向「舊 curr.random 對應的新 node」
                                                        #A'.random = B'
            curr = curr.next                            #這是把 curr 往後移到下一個舊節點。這裡走的還是原本的舊 list，不是新 list。

        return oldtonew[head]   #回傳舊 head 對應的新 head