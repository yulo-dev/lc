class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(r, c, i):
            # 成功條件：指標 i 走到單字末尾
            if i == len(word):
                return True
            
            # 失敗條件：越界、字母不對、或是踩到走過的地方 ('#')
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if board[r][c] != word[i]:
                return False

            
            # --- 選擇 (Choose) ---
            # 暫存原本字母，並標記為已訪問
            temp = board[r][c]
            board[r][c] = "#"
            
            # --- 探索 (Explore) ---
            # 往四個方向深挖
            found = (dfs(r + 1, c, i + 1) or 
                     dfs(r - 1, c, i + 1) or 
                     dfs(r, c + 1, i + 1) or 
                     dfs(r, c - 1, i + 1))
            
            # --- 撤銷 (Unchoose) ---
            # 重要！不管有沒有找到，都要把字母還原，讓後面的起點能用
            board[r][c] = temp
            
            return found

        # 遍歷矩陣尋找第一個字母的起點
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]: # 優化：只從第一個字母開始 DFS
                    if dfs(r, c, 0):
                        return True
        return False