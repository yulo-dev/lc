class Solution:

    def flip(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        self.flip(matrix)

        n = len(matrix)

        for row in range(n):
            left = 0
            right = len(matrix[0])-1

            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1