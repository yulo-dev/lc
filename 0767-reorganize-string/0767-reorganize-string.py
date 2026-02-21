class Solution:
    def reorganizeString(self, s: str) -> str:
        
        n = len(s)
        cnt = Counter(s)

        # 1. 數學邊界檢查 (Early Return)
        # 如果某個字元出現次數超過總長的一半（向上取整），絕對無法排開
        # 例如: "aaab", n=4, maxFreq=3, (4+1)//2 = 2, 3 > 2 故無法排開。
        maxFreq = max(cnt.values())
        if maxFreq > (n + 1) // 2:
            return ""

        # 2. max-heap: (-freq, char)
        heap = [(-f, ch) for ch, f in cnt.items()]
        heapq.heapify(heap)

        res = []

        # 3. 核心邏輯：每次從 Heap 拿出「最強」跟「次強」的兩個人
        while len(heap) >= 2:
            # 彈出目前次數最多的兩個不同字元
            f1, c1 = heapq.heappop(heap)
            f2, c2 = heapq.heappop(heap)

            # 將它們依序排入結果，因為 c1 != c2，所以這兩個絕對不重複
            res.append(c1)
            res.append(c2)

            f1 += 1  # 因為是負數，+1 代表用掉一次
            f2 += 1

            # 如果還沒用完，放回 Heap 參與下一輪競爭
            if f1 != 0:
                heapq.heappush(heap, (f1, c1))
            if f2 != 0:
                heapq.heappush(heap, (f2, c2))

        # 4. 收尾階段：檢查是否還有剩餘一個字元
        # 當 Heap 只剩 1 個元素時，while 迴圈會停止
        if heap:
            _, c = heapq.heappop(heap)
            res.append(c)

        return "".join(res)