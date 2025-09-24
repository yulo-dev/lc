class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, k, subset, res):
        res.append(subset[:])
        for i in range(k, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i+1, subset, res)
            subset.pop()