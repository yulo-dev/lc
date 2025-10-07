class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)
        
        for num in cnt:
            if cnt[num] == 1:
                return num