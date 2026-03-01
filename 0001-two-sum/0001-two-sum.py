class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()  # 按 num 排序

        left = 0
        right = len(arr) - 1

        while left < right:
            curr_sum = arr[left][0] + arr[right][0]

            if curr_sum == target:
                return [arr[left][1], arr[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
