class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return board

        visited = set()

        # 1) 只從邊界的 'O' 出發 BFS，把所有「邊界可達的 O」標成 'T'
        for x in range(len(board)):
            # 左邊界 (col = 0)
            if board[x][0] == "O" and (x, 0) not in visited:
                self.bfs(board, x, 0, visited)
            # 右邊界 (col = n-1)
            if board[x][len(board[0]) - 1] == "O" and (x, len(board[0]) - 1) not in visited:
                self.bfs(board, x, len(board[0]) - 1, visited)

        for y in range(len(board[0])):
            # 上邊界 (row = 0)
            if board[0][y] == "O" and (0, y) not in visited:
                self.bfs(board, 0, y, visited)
            # 下邊界 (row = m-1)
            if board[len(board) - 1][y] == "O" and (len(board) - 1, y) not in visited:
                self.bfs(board, len(board) - 1, y, visited)

        # 2) 掃盤：被包住的 'O' -> 'X'；安全的 'T' -> 'O'
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "T":
                    board[x][y] = "O"

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