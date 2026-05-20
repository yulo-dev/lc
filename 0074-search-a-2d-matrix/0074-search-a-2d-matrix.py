class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
       # 把2d展開成1d去思考
       left = 0
       right = len(matrix[0]) * len(matrix) - 1

       while left <= right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

       return False
