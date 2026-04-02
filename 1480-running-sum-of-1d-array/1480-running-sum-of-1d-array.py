class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        res = 0
        ans = []
        for x in nums:
            res += x
            ans.append(res)

        return ans