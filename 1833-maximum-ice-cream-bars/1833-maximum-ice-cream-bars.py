class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        if costs[0] > coins:
            return 0

        cnt = 0
        tot = 0
        for k in costs:
            if coins >= k:
                coins -= k
                cnt += 1
                tot = max(tot, cnt)
        
        return tot