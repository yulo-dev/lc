class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        
        res = 0

        for g in grid:
            i = 0
            while i < len(g):
                if g[i] < 0:
                    res += 1
                i += 1
                
        return res