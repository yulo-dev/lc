class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[len(nums)-2] + nums[len(nums)-1] < target:
                    continue
                 
                while left < right:
                    tot = nums[i] + nums[j] + nums[left] + nums[right]
                    if tot > target:
                        right -= 1
                    elif tot < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        left += 1
                        right -= 1

        return res
                        
                    
