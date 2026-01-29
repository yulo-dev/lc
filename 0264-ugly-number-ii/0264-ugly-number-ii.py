class Solution:
    def nthUglyNumber(self, n: int) -> int:

        #此時他就已經符合heap條件了 在 heapq 裡，「heap」不是一個獨立型別，它就是 一個滿足 heap property 的 list
        # 已經是合法 min-heap
        ugly_candidates = [1] 
        visited = set([1])

        val = None
        for i in range(n):
            val = heapq.heappop(ugly_candidates) #所以直接pop沒問題
            for factor in [2,3,5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(ugly_candidates, val * factor)
        return val
     