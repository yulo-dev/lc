class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n

        while left + 1 < right:
            mid = left + (right - left) // 2
            tot = mid * (mid + 1) // 2

            if tot <= n:
                left = mid
            elif tot > n:
                right = mid
            
        return left