class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]

                if val == ".":
                    continue 

                box = (i // 3) * 3 + j // 3

                if val in rows[i] or val in cols[j] or val in boxes[box]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                boxes[box].add(val)
                
        return True