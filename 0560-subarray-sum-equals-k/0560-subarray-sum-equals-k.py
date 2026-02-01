class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix sum + hashmap
        # Track:
        #   prefix: running sum up to current index
        #   freq[p]: how many times prefix sum p has occurred so far
        # Key idea:
        #   subarray sum = k  <=>  prefix - old_prefix = k  <=>  old_prefix = prefix - k
        # So at each step:
        #   ans += freq[prefix - k]
        # Then update:
        #   freq[prefix] += 1
        # Return:
        #   ans  (total number of subarrays whose sum equals k)

        count = defaultdict(int) 
        count[0] = 1

        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            ans += count[prefix-k] # 先用歷史去算答案
            count[prefix] += 1 # 再把現在加入歷史 #count是歷史 prefix sums 的頻率表
           

        return ans