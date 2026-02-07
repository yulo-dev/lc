class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)  # 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]  # 仍然是 9 個 box（因為 9x9）

        for i in range(n):
            for j in range(n):
                vals = board[i][j]

                if vals == ".":
                    continue


                #固定的映射公式
                #box row 0: [0] [1] [2]
                #box row 1: [3] [4] [5]
                #box row 2: [6] [7] [8]

                #Each 3 rows form a box-row and each 3 cols form a box-col. 
                #So (i//3, j//3) locates the box in a 3x3 grid, and we flatten it by boxRow*3 + boxCol.
                b = (i // 3) * 3 + j // 3

                if vals in rows[i] or vals in cols[j] or vals in boxes[b]:
                    return False

                rows[i].add(vals)
                cols[j].add(vals)
                boxes[b].add(vals)

        return True