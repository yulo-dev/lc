class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        #input & output:
        # Input: unsorted integer array
        # Output: length of the longest consecutive sequence

        ##clarification:
        # contain negative value? yes
        # input sorted? no
        # expected complexity? O(n)

        ##edge cases:
        # [] -> 0
        # [1,1,1,1] -> 1
        # [1,2,3] -> 3

        ##approach:
        # create a set of nums
        # find starting point: n-1 is not in the set
        # after finding the starting point: count the length (=length + 1) by finding the n+1 in the set
        # return the length

        uni_set = set(nums)

        res = 0

        for n in uni_set:
            if n-1 not in uni_set:
                start = n
                length = 1

                while start + 1 in uni_set:
                    length += 1
                    start += 1

                res = max(res, length)

        return res