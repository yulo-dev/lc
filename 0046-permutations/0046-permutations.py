class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        # 1. 點名表：記錄哪些數字已經在 path 裡面了
        used = [False] * len(nums)

        def backtracking():
            # 2. 終止條件：當 path 長度跟 nums 一樣，代表排完了！
            if len(path) == len(nums):
                res.append(path.copy()) # 拍照存證
                return

            # 3. 每一層都從頭遍歷所有數字
            for i in range(len(nums)):
                # 如果這個數字已經被用過了，跳過它
                if used[i]:
                    continue

                # --- 做選擇 (Choose) ---
                used[i] = True
                path.append(nums[i])
                # --- 探索 (Explore) ---
                backtracking()
                # --- 撤銷選擇 (Unchoose) ---
                path.pop()
                used[i] = False

        backtracking()
        return res