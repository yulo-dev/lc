class Solution:
    def maxArea(self, height: List[int]) -> int:

        area = 0
        x = 0
        y = 0

        left = 0
        right = len(height) - 1

        while left < right:
            x = right - left
            y = min(height[left], height[right])
            area = max(area, x*y)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
    
        return area