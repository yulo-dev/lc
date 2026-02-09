class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])

        dirs = [(-1,-1), (-1,0), (-1,1),
                (0,-1),          (0,1),
                (1,-1),  (1,0),  (1,1)]

        def live_neighbors(r: int, c: int) -> int:
            cnt = 0
            for dir_r, dir_c in dirs:
                new_r, new_c = r + dir_r, c + dir_c
                if 0 <= new_r < m and 0 <= new_c < n:
                    # 1 or 2 表示「原本是活的」
                    if board[new_r][new_c] == 1 or board[new_r][new_c] == 2:
                        cnt += 1
            return cnt


        # 1) 第一趟：用 2/3 標記過渡狀態
        # 1: 原本活
        # 2: 原本也活（只是下一輪要死）
        # 3: 原本死（只是下一輪要活）
        # 4: 原本死
        for r in range(m):
            for c in range(n):
                live_cnt = live_neighbors(r, c)

                if board[r][c] == 1:
                    # 活 cell：少於 2 或多於 3 會死
                    if live_cnt < 2 or live_cnt > 3:
                        board[r][c] = 2  # 1 -> 0
                else:
                    # 死 cell：剛好 3 個活鄰居會活
                    if live_cnt == 3:
                        board[r][c] = 3  # 0 -> 1

        # 2) 第二趟：把過渡狀態轉成新狀態
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1