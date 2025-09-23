class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        if not nums:
            return []
            
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], res)
        return res

    def dfs(self, nums, visited, subset, res):
        if len(subset) == len(nums):
            res.append(subset[:])

        for i in range(len(nums)):
            if visited[i] == True:
                continue

            subset.append(nums[i])
            visited[i] = True

            self.dfs(nums, visited, subset, res)

            subset.pop()
            visited[i] = False
