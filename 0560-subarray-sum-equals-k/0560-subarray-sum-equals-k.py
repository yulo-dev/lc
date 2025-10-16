class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_sum = 0
        cnt = 0
        visited = {0:1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in visited:
                cnt += visited[prefix_sum - k]

            visited[prefix_sum] = visited.get(prefix_sum, 0) + 1

        return cnt