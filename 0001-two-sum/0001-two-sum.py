class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visit = {} #{nums: index}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in visit:
                return [visit[comp], i]

            visit[n] = i