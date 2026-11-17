class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        
        left = 0
        right = len(letters) 

        while left < right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1

        return letters[left] if left < len(letters) else letters[0]