class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        left = 0
        right = len(numbers) - 1

        while left < right:
            tot = numbers[left] + numbers[right]
            if tot > target:
                right -= 1
            elif tot < target:
                left += 1
            else:
                return [left + 1, right + 1]