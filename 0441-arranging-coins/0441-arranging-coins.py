class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0 
        right = n 

        while left + 1 < right:
            mid = left + (right - left) // 2
            val = mid * (mid + 1) // 2

            if val <= n:
                left = mid
            else:
                right = mid
        
        if right * (right + 1) // 2 <= n:
            return right

        if left * (left + 1) // 2 <= n:
            return left