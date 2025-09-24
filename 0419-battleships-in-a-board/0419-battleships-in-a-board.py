class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        res = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == "X":
                    if (j > 0 and board[i][j - 1] == "X") or (i > 0 and board[i -1][j] == "X"):
                        continue
                    res += 1
        return res