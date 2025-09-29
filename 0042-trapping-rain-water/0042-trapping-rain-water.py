class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n - 1):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax[n -1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        water = 0
        for i in range(n-1):
            water += min(leftMax[i], rightMax[i]) - height[i]

        return water
        