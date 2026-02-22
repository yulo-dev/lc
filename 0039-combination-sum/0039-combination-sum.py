class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        
        candidates.sort()

        def backtracking(remain, start):
            if remain == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                backtracking(remain - candidates[i], i)
                path.pop()

        backtracking(target, 0)
        return res