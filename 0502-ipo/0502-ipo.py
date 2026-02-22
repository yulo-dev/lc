class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # 1. 將項目組合成 (required_capital, profit) 並按 capital 從小到大排序
        # 這樣我們才能依序「解鎖」買得起的項目
        projects = sorted(zip(capital, profits))  
        i = 0
        max_heap = []  # store -profit

        # 2. 執行 k 輪投資
        for _ in range(k):
            # 1) 把所有目前資產 w 買得起的項目，通通丟進 Max-Heap
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # 2) # 如果目前沒有買得起的項目，就提早結束
            if not max_heap:
                break

            # 3) 貪婪選擇：做獲利最高的項目
            w += -heapq.heappop(max_heap)

        return w


#greedy: 想資產最大化，在所有「買得起」的項目裡，永遠選「獲利最高」的那個
#max heap:存目前「買得起」的所有項目的獲利

#想像在逛超市，有些商品很貴現在買不起。
#先去架子上看最便宜的區塊。
#把所買得起的東西，根據「 CP 值（獲利）」丟進購物籃。
#每次從籃子裡拿出一個最賺的東西吃掉。
#吃完後變有錢了，可以再去超市解鎖更貴、更高利潤的區塊。