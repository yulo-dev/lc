class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtracking():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                #選
                used[i] = True
                path.append(nums[i])
                #expand
                backtracking()
                #撤回
                path.pop()
                used[i] = False

        backtracking()
        return res