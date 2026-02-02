class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        step = 1

        for ch in s:
            rows[row] += ch

            #只有在頂部跟底部會走到這塊if else的條件 其他step就是沿用當時的方向 去+1or -1
            #只有在頂部 row == 0 或底部 row == numRows - 1 的時候才會改方向
            #其他時間 step 沿用上一輪的方向（一直往下 or 一直往上）
            #step 只在「撞牆」（最上/最下）時翻轉，平常就照原方向一直走
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1

            row += step

        return "".join(rows)
