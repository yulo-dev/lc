class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        mapping = defaultdict(int)
        uni_nums = set(nums)

        dup = None

        for n in nums:
            mapping[n] += 1
            if mapping[n] > 1:
                dup = n

        for n in range(1, len(nums)+1):
            if n not in uni_nums:
                return [dup, n]

