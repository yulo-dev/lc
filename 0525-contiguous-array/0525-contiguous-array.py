class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        # view 0 as -1,  1 as 1
        # calculate the prefix sum
        # store the index & prefix sum in hashmap, prefix sum = key, index = value
        # if two place got the same prefix sum, then the number between them should have equal 0,1


        prefix = [0] * (len(nums) + 1)
        hashmap = {}
        hashmap[0] = 0

        res = 0

        for i in range(1, len(nums) + 1):

            format_num = -1 if nums[i-1] == 0 else 1

            prefix[i] = prefix[i-1] + format_num

            if prefix[i] in hashmap:
                res = max(res, i - hashmap[prefix[i]])
            else:
                hashmap[prefix[i]] = i

        return res
