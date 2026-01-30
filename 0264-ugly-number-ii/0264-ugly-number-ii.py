class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_candidates = [1]
        visited = set([1])

        #ㄐfor loop它不控制 candidate 數量，它控制的是 pop 次數（也就是輸出第幾個）
        for i in range(n):
            val = heapq.heappop(ugly_candidates)
            for factor in [2,3,5]:
                if val * factor not in visited:
                    heapq.heappush(ugly_candidates, val * factor)
                    visited.add(val * factor)

        return val