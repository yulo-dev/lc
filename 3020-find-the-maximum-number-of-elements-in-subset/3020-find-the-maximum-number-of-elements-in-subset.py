class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        cnt = Counter(nums)
        uni = set(nums)
        res = 0 

        for x in uni:
            count = 0
            curr = x

            if x == 1:
                if cnt[1] % 2 == 0:
                    count = cnt[1] - 1
                else:
                    count = cnt[1]

            else:      
                count = 0  
                while curr * curr in cnt and cnt[curr] >= 2 and x > 1:
                    count += 2
                    curr = curr * curr
                    
                count = count + 1

            res = max(res, count)

        return res