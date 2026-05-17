class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height) 
        
        left = 0 
        right = n - 1
        max_left = 0
        max_right = 0
        area = 0

        while left < right:
            if height[left] <= height[right]:
                max_left = max(height[left], max_left)
                area += max_left - height[left]
                left += 1
            if height[left] > height[right]:
                max_right = max(height[right], max_right)
                area += max_right - height[right]
                right -= 1

        return area