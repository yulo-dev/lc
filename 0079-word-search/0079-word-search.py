class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        

        #k 是什麼？ 它代表「目前我已經湊到了單字的第幾個字母」
        def backtracking(r, c, k):
            # 1. 成功條件：字湊齊了
            if k == len(word):
                return True
            
            # 2. 失敗條件 (剪枝)：
            # - 越界 (超出網格)
            # - 字母不對
            # - 踩到已訪問過的格子 (我們之後會把走過的地方改成 "#")
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if board[r][c] != word[k]:
                return False

            
            # --- 選擇 (Choose) ---
            temp = board[r][c] # (1) 記住原本這裡是什麼字 (例如 'A')
            board[r][c] = "#"  # (2) 把地圖弄髒，代表「這格我現在踩著，不準回頭踩」
                               # 如果你不把它改成 #，特務可能會在兩個字母之間來回跳（例如 A -> B -> A），陷入死循環
            
            # --- 探索 (Explore) ---
            # 往四個方向嘗試，只要有一個方向通，就回傳 True
            found = (backtracking(r + 1, c, k + 1) or 
                     backtracking(r - 1, c, k + 1) or 
                     backtracking(r, c + 1, k + 1) or 
                     backtracking(r, c - 1, k + 1))
            
            # --- 撤銷 (Unchoose) ---
            # 這是 Backtracking 的靈魂！一定要把字母還原，不然下一個起點就沒得玩了
            # 把 '#' 改回原本的字母 (例如 'A')
            # 為什麼要改回來？ 假設你從 (0,0) 開始找 APPLE 失敗了。接著外層迴圈試試從 (0,1) 開始找。
            # 如果剛才 (0,0) 踩過的痕跡沒擦掉，(0,1) 出發的路徑如果需要經過 (0,0)，它就會看到一堆 # 而失敗
            board[r][c] = temp
            
            return found

        # 外層迴圈：你不知道這個單字會從地圖的哪一格開始. 所以必須把地圖上的每一格都當成「起點」試試看
        for r in range(m):
            for c in range(n):
                if backtracking(r, c, 0):
                    return True
        return False