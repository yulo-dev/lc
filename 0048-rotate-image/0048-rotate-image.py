class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

         # 1) transpose: swap (i, j) with (j, i) for j > i
         # 先transpose, 欄變列, 列變欄
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2) reverse each row
        # 再每一列反轉
        for row in matrix:
            row.reverse()