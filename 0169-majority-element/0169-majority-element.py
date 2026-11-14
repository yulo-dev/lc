class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        candidate = None
        cnt = 0

        for n in nums:
            if cnt == 0 or n == candidate:
                candidate = n
                cnt += 1
            else:
                cnt -= 1

        return candidate