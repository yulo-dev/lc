# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 1
        right = n 

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid # mid 可能是第一個 bad，往左收
            else:
                left = mid + 1 # mid 不是 bad，第一個 bad 一定在右邊

        return left