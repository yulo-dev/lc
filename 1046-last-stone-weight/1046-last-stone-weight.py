class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h) > 1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)
            diff = a - b
            if diff != 0:
                heapq.heappush(h, -diff)

        return -h[0] if len(h) == 1 else 0



#這題因為要抓max heap, 所以要先把list的數字轉成負的, 再做heapify
#接著需要至少有兩顆石頭才能比：
    #兩個最重的石頭 如果有大小之分, 就相減 把這個差值丟回heap
    #如果兩個重量相同, 就不push回去, 就代表兩個都消失了