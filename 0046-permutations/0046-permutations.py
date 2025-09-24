class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, subset, res):
        if len(subset) == len(nums):
            res.append(subset[:])
            return

        for i in range(len(nums)):
            if visited[i] != True:
                subset.append(nums[i])
                visited[i] = True
                self.dfs(nums, visited, subset, res)
                subset.pop()
                visited[i] = False