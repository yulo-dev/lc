class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()

        cnt = 0
        for k in costs:
            if coins >= k:
                coins -= k
                cnt += 1
        
        return cnt