class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        cnt = 0
        visit = {0:1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in visit:
                cnt += visit[prefix_sum - k]
            visit[prefix_sum] = visit.get(prefix_sum, 0) + 1
        return cnt