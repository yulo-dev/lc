class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_candidates = [1]
        visited = set([1])

        for i in range(n): #這邊的i 每一次就是pop一個數 所以走到n就是pop n次 最後一次的pop val就是結果
            val = heapq.heappop(ugly_candidates)
            for factor in [2,3,5]:
                if val * factor not in visited:
                    heapq.heappush(ugly_candidates, val * factor)
                    visited.add(val * factor)
        
        return val

#這段在做：
#heap 一開始只有 1（第 1 個 ugly）
#每次從 heap 拿出目前最小的 ugly（heappop）
#用它生成新的 ugly 候選（×2, ×3, ×5）
#丟進 heap（用 visited 去重）
#重複 n 次 pop
#所以：
#第 1 次 pop： 拿到 1（第 1 個 ugly）
#第 2 次 pop： 拿到 2（第 2 個 ugly）
#第 3 次 pop： 拿到 3
#…
#在 for loop 裡 heappop 了 n 次，那最後一次 pop 的 val 就是答案。
