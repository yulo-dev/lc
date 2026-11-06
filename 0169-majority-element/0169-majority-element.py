class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        cnt = 0

        for i in range(len(nums)):
            if cnt == 0:
                candidate = nums[i]

            if nums[i] == candidate:
                cnt += 1
            else:
                cnt -= 1
            
        return candidate