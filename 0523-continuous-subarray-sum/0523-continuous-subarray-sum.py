class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        

        # get the prefix sum & the remainder after devided by 6
        # store the index & remainder in a hashmap, remainder = key, index = value
        # then check if key exists in the map, if it is then return true

        ##

        prefix = [0] * (len(nums) + 1)
        hashmap = {}
        hashmap = {0: 0}

        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
            remainder = prefix[i] % k 
            if remainder not in hashmap:
                hashmap[remainder] = i

            else:
                if i - hashmap[remainder] >= 2:
                    return True
            
        return False