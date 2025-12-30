class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()

        left = 0
        right = 1
        gap = arr[right] - arr[left]
        
        while right < len(arr):
            if arr[right] - arr[left] != gap:
                return False
            left += 1
            right += 1

        return True