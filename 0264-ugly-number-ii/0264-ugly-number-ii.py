class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_candidates = [1]

        #python的set是hashset 是哈希表
        visited = set([1])

        val = None
        for i in range(n):
            val = heapq.heappop(ugly_candidates)
            for factor in [2,3,5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(ugly_candidates, val * factor) #time: logn

        return val
        
        #time: O(nolgn)
        #space: O(n) heap+visited
        
        #他的概念是從1, 2, 3, 5開始 然後先拿出最小的1, 之後拿出2, 跟剩下的3,5 去乘 累積更多的數 然後反覆從裡面抓最小的出來
        #所以有add, min -> heap + 去除重複的 -> hashset

        #從 1 開始，每次取出目前最小的 ugly x，把 2x, 3x, 5x 推回 heap。
        #為了避免重複（例如 2×3 與 3×2），用 seen set 只 push 沒出現過的。