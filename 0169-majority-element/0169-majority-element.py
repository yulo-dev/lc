class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        candidate = 0
        cnt = 0

        for n in nums:
            if cnt == 0:
                candidate = n
                cnt += 1
            elif n == candidate:
                cnt += 1
            elif n != candidate:
                cnt -= 1

        return candidate