class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        cnt = 0

        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += 1 if num == candidate else -1
        return candidate