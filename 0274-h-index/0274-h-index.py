class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        count = [0] * (n + 1)

        #把 citation 壓縮成 0..n 的分布: 把原本「很散的數值」轉成「固定範圍的統計」
        for c in citations:
            #Cap（上限壓縮）: 因為100 和 n 的角色一樣：都是 “很大的一篇”, h 不可能 > n
            if c >= n:
                count[n] += 1
            #保留精確分布（0..n-1）: 小於 n 的才分到各自桶
            else:
                count[c] += 1


        #從大到小掃：維護 papers = #papers with citations >= h
        papers = 0
        for h in range(n, -1, -1):
            papers += count[h] #papers 永遠是目前累積到的「高引用論文總數」

            if papers >= h: #papers 代表 “≥ h 的論文篇數”
                return h
        return 0