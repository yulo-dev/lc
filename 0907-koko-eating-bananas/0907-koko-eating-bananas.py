class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        while left + 1 < right:
            mid = left + (right - left) // 2
            
            tot = 0
            for p in piles:
                tot += ceil(p / mid)
            
            if tot <= h:
                right = mid
            else:
                left = mid

        est = sum(ceil(p / left) for p in piles)
        if est <= h:
            return left
        return right