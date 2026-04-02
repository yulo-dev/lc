class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        res = 0
        
        for acc in accounts:
            temp = 0
            for x in acc:
                temp += x
            res = max(res, temp)

        return res