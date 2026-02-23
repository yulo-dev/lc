from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        islands = 0
        
        for r in range(m):
            for c in range(n):
                # 1. 發現新島嶼的「起點」
                if grid[r][c] == "1":
                    islands += 1
                    # 2. 發動 DFS 把它淹沒
                    self.dfs(grid, r, c)
        
        return islands

    def dfs(self, grid, r, c):
        # --- 邊界檢查與終止條件 ---
        # 如果超出邊界，或是這格已經是水 ("0")，就撤退
        if (r < 0 or c < 0 or 
            r >= len(grid) or c >= len(grid[0]) or 
            grid[r][c] == "0"):
            return
        
        # --- 做標記 (淹沒陸地) ---
        # 把這格改成 "0"，確保外層迴圈和未來的遞迴不會重複計算
        grid[r][c] = "0"
        
        # --- 往四周深挖 (四個方向) ---
        self.dfs(grid, r + 1, c) # 下
        self.dfs(grid, r - 1, c) # 上
        self.dfs(grid, r, c + 1) # 右
        self.dfs(grid, r, c - 1) # 左

        #我們的目標是「把這團相連的陸地標記完」，標記完了就是完了，這格已經完成了它的使命，
        #不需要再變回 1 -> 不需要回溯
        #邏輯： 只要這塊地被我「淹掉」了（從 1 變成 0），它就永遠失去了作為「新起點」的資格。
        #LC 200 是「破壞性」的搜尋：拆掉這座島，數 1 次，就再也不回頭