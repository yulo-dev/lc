class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)] #算有幾個鄰居
        in_degree = [0] * n #算每個點連幾條邊

        for u, v in edges:
            graph[u].append(v) #把 v 加到 u 的鄰居清單
            graph[v].append(u)
            in_degree[u] += 1 #u 多一個鄰居
            in_degree[v] += 1


        queue = deque()
        for i in range(n): 
            if in_degree[i] == 1: #第一層葉子 因為i 只連一條邊 → i 是葉子
                queue.append(i) #把所有葉子丟進 queue

        remaining = n #用來判斷還剩下多少葉子

        #樹的中心就是「直徑的中點」, 直徑 = 樹中最長的一條路徑（兩端一定是葉子）, 
        #你要讓高度最小，root 一定要站在「最長路徑的中間」，不然到兩端會更遠
        #而「一條路徑的中點」會是：
        #路徑長度（邊數）偶數 → 中點是 1 個節點
        #路徑長度（邊數）奇數 → 中點是 2 個相鄰節點
        while remaining > 2: 
            size = len(queue) #這一輪要移除「整層」葉子, size是這一圈葉子數
            remaining -= size #把這一圈葉子全部剝掉

            #剝掉葉子後更新
            for _ in range(size):
                leaf = queue.popleft()
                for nei in graph[leaf]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 1: #如果鄰居變成 degree == 1，代表它成為新葉子 → 加進 queue
                        queue.append(nei)

        return list(queue) #在題目保證是「樹」的前提下（連通、無環），一定找得到。
        