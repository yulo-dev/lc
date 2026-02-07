class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                vals = board[i][j]

                if vals == ".":
                    continue

                b = (i // 3) * 3 + (j // 3)

                if vals in rows[i] or vals in cols[j] or vals in boxes[b]:
                    return False

                rows[i].add(vals)
                cols[j].add(vals)
                boxes[b].add(vals)

        return True