class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        min_pile = 1
        max_pile = max(piles)

        while min_pile < max_pile:
            mid_pile = (min_pile + max_pile) // 2

            hours = 0

            #calculate hours needed
            for pile in piles:
                if pile % mid_pile > 0:
                    hours += pile // mid_pile + 1
                else:
                    hours += pile // mid_pile

            #leftmost
            if hours <= h:
                 max_pile = mid_pile
            else:
                min_pile = mid_pile + 1

        return min_pile
        