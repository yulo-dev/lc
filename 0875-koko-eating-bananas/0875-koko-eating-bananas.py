class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        def can_finish(speed):
            hours = 0
            for p in piles:
                hours += (p + speed - 1) // speed
            return hours <= h

        while left <= right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res