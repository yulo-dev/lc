class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates:
            return []

        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, k, subset, res):

        if target == 0:
            res.append(subset[:])
            return
        if target < 0:
            return

        for i in range(k, len(candidates)):
            subset.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, subset, res)
            subset.pop()