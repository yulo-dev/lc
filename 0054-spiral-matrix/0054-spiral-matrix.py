class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
    
        m = len(matrix)
        n = len(matrix[0])

        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []

        while top <= bottom and left <= right:
            # 1) top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # 2) right col
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # 3) bottom row (if still valid)
            # 加上if條件是因為走完前兩邊（top row、right col）後，你把邊界縮小了
            # 這時候可能已經沒有剩下的 row 或 col 了
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # 4) left col (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res