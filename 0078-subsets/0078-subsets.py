class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, start, subset, res):
        res.append(subset[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i+1, subset, res)
            subset.pop()