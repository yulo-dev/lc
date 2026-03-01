class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i-1])

        right_max[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        tot = 0
        for i in range(len(height)):
            tot += min(left_max[i], right_max[i]) - height[i]

        return tot

#My plan is to preprocess the array in two passes.
#In the first pass, I record the highest wall to the left of each index.
#In the second pass, I record the highest wall to the right of each index.
#Once I have those two arrays, I can compute how much water each position can hold. 
#The water level is determined by the shorter boundary between the left max and the right max, and then I subtract the current height.
#Finally, I add up the trapped water for all positions.