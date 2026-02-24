class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return board

        row = len(board)
        col = len(board[0])

        visited = set()

        # 1) 只從邊界的 'O' 出發 BFS，把所有「邊界可達的 O」標成 'T'
        for r in range(row):
            # 左邊界 (col = 0)
            if board[r][0] == "O" and (r, 0) not in visited:
                self.bfs(board, r, 0, visited)
            # 右邊界 (col = n-1)
            if board[r][len(board[0]) - 1] == "O" and (r, len(board[0]) - 1) not in visited:
                self.bfs(board, r, len(board[0]) - 1, visited)

        for c in range(col):
            # 上邊界 (row = 0)
            if board[0][c] == "O" and (0, c) not in visited:
                self.bfs(board, 0, c, visited)
            # 下邊界 (row = m-1)
            if board[len(board) - 1][c] == "O" and (len(board) - 1, c) not in visited:
                self.bfs(board, len(board) - 1, c, visited)

        # 2) 掃盤：被包住的 'O' -> 'X'；安全的 'T' -> 'O'
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        return 

    def bfs(self, board, x, y, visited):
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque([(x,y)])
        visited.add((x,y))
        board[x][y] = "T"

        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in DIRECTIONS:
                new_x = dir_x + x
                new_y = dir_y + y
                if not self.is_valid(board, new_x, new_y, visited):
                    continue
                board[new_x][new_y] = "T"
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
    
    def is_valid(self, board, x, y, visited):
        m = len(board)
        n = len(board[0])

        if not (0 <= x < m and 0<= y < n):
            return False
        if (x,y) in visited:
            return False
        return board[x][y] == "O"