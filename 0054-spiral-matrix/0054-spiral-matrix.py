class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        row_n = len(matrix)
        col_n = len(matrix[0])

        top = 0
        bottom = row_n - 1

        left = 0
        right = col_n - 1

        res = []

        while len(res) < (row_n * col_n):
            
            if top <= bottom:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
            
            if left <= right:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1

            if top <= bottom:
                for i in range(right, left -1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


