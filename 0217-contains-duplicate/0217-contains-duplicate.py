class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uni = set(nums)

        return len(nums) != len(uni)