class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0] * (len(nums) + 1)

        hashmap = defaultdict(int)
        hashmap[0] = 1 #因為它代表一個「起點狀態」而且這個狀態我們算它「出現過一次」

        res = 0

        for i in range(1, len(nums)+1):
            
            prefix[i] = prefix[i-1] + nums[i-1]

            #這有點算用回推的 new prefix - old prefix = k -> old prefix = new prefix - k 
            diff = prefix[i] - k

            if diff in hashmap:
                res += hashmap[diff]

            #最後才更新最新的prefix的freq 以免剛剛前面就把它算進去
            hashmap[prefix[i]] += 1

        return res