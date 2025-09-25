class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if not candidates:
            return []

        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, candidates, target, start, subset, res):
        if target == 0:
            return res.append(subset[:])

        if target < 0:
            return

        for i in range(start, len(candidates)):
            subset.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, subset, res)
            subset.pop()