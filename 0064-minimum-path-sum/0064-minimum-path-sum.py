class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        #這題因為權重不同 所以如果要用bfs 要用Dijkstra

        #這題規定只能「向右」或「向下」，這意味著要到達任何一個格子 (r, c)
        #你只有兩個來源：從上面掉下來：(r-1, c)$從左邊走過來：(r, c-1)

        rows = len(grid)
        cols = len(grid[0])

        # first row
        # 只能從左邊來
        for c in range(1, cols):
            grid[0][c] += grid[0][c - 1]

        # first col
         # 只能從上面來
        for r in range(1, rows):
            grid[r][0] += grid[r - 1][0]

        # fill the rest
        # 關鍵：取上方與左方的最小值
        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[rows - 1][cols - 1]