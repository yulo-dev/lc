class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

         # 1) transpose: swap (i, j) with (j, i) for j > i
         # 先transpose, 欄變列, 列變欄
         # 他的做法是沿著對角線做「鏡射」: 對角線是 (0,0), (1,1), (2,2)
         ####### col0   col1   col2
         #row0   (0,0)  (0,1)  (0,2)
         #row1   (1,0)  (1,1)  (1,2)
         #row2   (2,0)  (2,1)  (2,2)
         # 所以就是(0,1) <-> (1,0), (0,2) <-> (2,0), (1,2) <-> (2,1)

        # 只做上半矩陣
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2) reverse each row
        # 再每一列反轉
        for row in matrix:
            row.reverse()