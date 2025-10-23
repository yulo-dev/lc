class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1           # Minimum possible eating speed
        right = max(piles) # Maximum needed eating speed

        while left + 1 < right:
            mid = left + (right - left) // 2  

            # Calculate total hours needed at speed 'mid'
            hours = 0
            for p in piles:
                hours += ceil(p/mid)

            if hours <= h:
                right = mid
            else:
                left = mid

        time_left = sum(ceil(p / left) for p in piles)
        if time_left <= h:
            return left
        return right