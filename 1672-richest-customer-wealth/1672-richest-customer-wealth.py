class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        res = 0
        for acc in accounts:
            current = sum(acc)
            res = max(res, current)
        return res