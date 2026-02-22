class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        
        # 為了優化 (剪枝)，我們可以先排序
        candidates.sort()
        
        def backtrack(remain, start):
            # 1. 終止條件
            if remain == 0:
                res.append(path.copy())
                return
            
            # 2. 橫向遍歷候選人
            for i in range(start, len(candidates)):
                # --- 剪枝 (Pruning) ---
                # 如果目前的數字已經大於剩下的目標，後面的數字更不可能，直接停掉
                if candidates[i] > remain:
                    break
                
                # 做選擇
                path.append(candidates[i])
                
                # --- 探索 (Explore) ---
                # 重點在此：傳入 i 而不是 i + 1
                # 這代表下一層遞迴「依然可以從自己開始選」，達成重複使用
                backtrack(remain - candidates[i], i)
                
                # 撤銷選擇
                path.pop()
        
        backtrack(target, 0)
        return res