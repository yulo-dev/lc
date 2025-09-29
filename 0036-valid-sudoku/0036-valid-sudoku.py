class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                vals = board[i][j]

                if vals == ".":
                    continue

                b = (i // 3) * 3 + j // 3

                if vals in rows[i] or vals in cols[j] or vals in boxes[b]:
                    return False

                rows[i].add(vals)
                cols[j].add(vals)
                boxes[b].add(vals)
        return True