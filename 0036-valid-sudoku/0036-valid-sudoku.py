class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                vals = board[r][c]
                if vals == ".":
                    continue

                box = (r // 3) * 3 + (c // 3)

                if vals in rows[r] or vals in cols[c] or vals in boxes[box]:
                    return False  

                rows[r].add(vals) 
                cols[c].add(vals) 
                boxes[box].add(vals) 

        return True
