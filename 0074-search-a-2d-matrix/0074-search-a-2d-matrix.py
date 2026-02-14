class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False