class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        cnt = 0

        for n in nums:
            if cnt == 0:
                candidate = n
            cnt += 1 if n == candidate else -1
        return candidate