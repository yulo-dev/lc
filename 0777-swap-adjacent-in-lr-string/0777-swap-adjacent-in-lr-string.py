class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace("X", "") != result.replace("X", ""):
            return False

        n = len(start)
        i = j = 0

        # 只要任一邊還沒掃完，都要繼續，才能檢查「有沒有一邊還剩 piece」
        while i < n or j < n:

            #skip X
            while i < n and start[i] == "X":
                i += 1
            while j < n and result[j] == "X":
                j += 1

            #兩邊都到尾巴了：start 沒有任何 L/R 可以比了, target 也沒有任何 L/R 可以比了
            if i == n and j == n:
                return True

            # 只有一邊到尾巴、另一邊還沒到: 一邊字母用完了，另一邊還有字母，表示對不上，直接不可能
            if i == n or j == n:
                return False

            # same piece type (L/R) due to the replace-check, but keep it safe:
            # 在對齊「第 k 個 piece」時，兩邊必須是同一種字母
            if start[i] != result[j]:
                return False

             # L would move right 
             # 例如 start: "LXX" -> end: "XXL" 做不到
             # start: "XL" -> end: "LX" 做得到
            if start[i] == "L" and j > i:  
                return False

            # R would move left
            # 例如 start: "XR" -> end: "RX" 做不到
             # start: "RXX" -> end: "XXR" 做得到
            if start[i] == "R" and j < i:  
                return False

            i += 1
            j += 1

        return True
        