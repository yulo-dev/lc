class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        
        res = 0

        for g in grid:
            left = 0
            right = len(g)
            while left < right:
                mid = (left + right) // 2
                if g[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid 

            res += len(g) - left 
            
        return res