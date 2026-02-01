class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = defaultdict(int)
        count[0] = 1

        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            ans += count[prefix - k]   # how many previous prefix sums make sum k
            count[prefix] += 1

        return ans