class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1

        return ans