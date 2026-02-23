class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        for r in range(m):
            for c in range(n):
                # 發現新陸地且沒去過，就發動 DFS 鑽到底
                if grid[r][c] == 1 and (r, c) not in visited:
                    # DFS 會直接回傳這座島的「總面積」
                    current_area = self.dfs(grid, r, c, visited)
                    max_area = max(max_area, current_area)
                    
        return max_area

    def dfs(self, grid, r, c, visited):
        # 1. 終止條件 (Base Cases)
        # 如果超出邊界、踩到水、或是這格已經算過了，貢獻面積就是 0
        if (r < 0 or r >= len(grid) or 
            c < 0 or c >= len(grid[0]) or 
            grid[r][c] == 0 or (r, c) in visited):
            return 0
        
        # 2. 標記已訪問 (打卡)
        visited.add((r, c))
        
        # 3. 核心遞迴邏輯：1 (自己) + 往四個方向鑽
        # 想像你在這格喊一聲，四個鄰居會把他們負責的那塊面積報數給你
        return (1 + 
                self.dfs(grid, r + 1, c, visited) + # 下
                self.dfs(grid, r - 1, c, visited) + # 上
                self.dfs(grid, r, c + 1, visited) + # 右
                self.dfs(grid, r, c - 1, visited))  # 左