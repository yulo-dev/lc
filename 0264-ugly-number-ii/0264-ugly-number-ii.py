class Solution:
    def nthUglyNumber(self, n: int) -> int:

        ugly_candidates = [1]
        visited = set([1])

        for i in range(n):
            val = heapq.heappop(ugly_candidates)
            for factor in [2,3,5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(ugly_candidates, val * factor)

        return val