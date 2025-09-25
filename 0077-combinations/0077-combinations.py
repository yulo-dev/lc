class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, 1, [], res)
        return res
    
    def dfs(self, n, k, start, subset, res):
        if len(subset) == k:
            return res.append(subset[:])
        
        for i in range(start, n + 1):
            subset.append(i)
            self.dfs(n, k, i + 1, subset, res)
            subset.pop()