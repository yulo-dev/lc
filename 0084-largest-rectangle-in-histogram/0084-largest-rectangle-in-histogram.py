class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) #讓最後一定會把剩下的柱子全部 pop 計算完
        indices_stack = [] #存 index
        area = 0

        for index, height in enumerate(heights ):
            while indices_stack and heights[indices_stack[-1]] >= height: #如果列表尾部高度大於當前高度
                popped_index = indices_stack.pop()
                left_index = indices_stack[-1] if indices_stack else -1		
                width = index - left_index - 1	 #如果列表是空的，則寬度為index，否則是index-indices_stack[-1]-1
                area = max(area, width * heights[popped_index])
                
            indices_stack.append(index)		
            
        return area

# [1,1] -> 2
# [0] -> 0
# [4,2] -> 4  