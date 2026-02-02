class Solution:
    def canChange(self, start: str, target: str) -> bool:

        #這題真正「不會變」的只有兩件事：
            # 1) L/R 的相對順序（它們不能互相穿越）
            # 2) 每個 piece 的移動方向限制（L 只能往左、R 只能往右）

        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        n = len(start)

        i = j = 0

        while i < n or j <n:
            # skip blank
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1
        
            # both finished
            # i == n 且 j == n：兩邊都沒有剩下的 L/R 了 → 代表全部 piece 都已經對齊檢查完了
            if i == n and j == n:
                return True

            # one finished earlier
            # (start 沒字母了，target 還有字母) 或是 (target 沒字母了，start 還有字母)
            if i == n or j == n:
                return False

            # piece type must match
            # i<n 且 j<n：兩邊都有下一個 piece → 才能安全地做：start[i] != target[j] 類型是否相同
            # 所以順序一定要是：先處理「有沒有字母可比」→ 再比字母與方向
            if start[i] != target[j]:
                return False

            # movement constraints
            if start[i] == 'L' and j > i:
                return False
            if start[i] == 'R' and j < i:
                return False

            i += 1
            j += 1

        return True
            