class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)
        
        hashmap = defaultdict(int)
        hashmap[0] = 1

        res = 0

        for i in range(1, len(nums)+1):
            
            prefix[i] = prefix[i-1] + nums[i-1]

            diff = prefix[i] - k

            if diff in hashmap:
                res += hashmap[diff]

            hashmap[prefix[i]] += 1

        return res