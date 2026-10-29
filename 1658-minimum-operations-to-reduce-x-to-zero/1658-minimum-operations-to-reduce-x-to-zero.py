class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        #expand right: not yet reach target
        #expand left: > target
        #updat res: when reach target

        left = 0
        right = 0
        target = sum(nums) - x #重點是這個轉換 他要先獲得最大的數列來組成target 以換取最小的數字可以把x減成0
        curr = target
        res = float("inf")

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        while right < len(nums):
            curr -= nums[right]
            right += 1

            while curr <= 0:
                if curr == 0:
                    res = min(res, len(nums) - (right - left))
                
                curr += nums[left]
                left += 1 

        return res if res != float("inf") else -1
    
        