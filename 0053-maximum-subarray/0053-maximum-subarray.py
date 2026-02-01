class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i]) #cur =「以 i 結尾」的最大子陣列和
            best = max(best, curr) #best = 到目前為止（掃到 i 為止）看過的最大子陣列和

        return best