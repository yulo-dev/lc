class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        #res可直接設成某三數和
        #res = float("inf")
        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                tot = nums[i] + nums[left] + nums[right]
                if tot == target:
                    return tot
                elif tot > target:
                    if abs(tot - target) < abs(res - target):
                        res = tot
                    right -= 1
                elif tot < target:
                    if abs(tot - target) < abs(res - target):
                        res = tot
                    left += 1

        return res
