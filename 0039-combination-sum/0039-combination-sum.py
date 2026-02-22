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

#1.排序：如果 candidates 是 [7, 2, 3]，當你看到 7 發現太大時，你不能確定後面的 2, 3 是不是也太大。但如果排序成 [2, 3, 7]，只要 3 太大，後面的 7 就絕對不用看了 —> 剪枝動作對於數字很大的遞回來說非常重要, 剪枝不僅僅是少跑幾次迴圈，它是剪掉了整棵子樹

#2.因為數字可以重複 只是組合不能重複 所以不需要used, used是用來控制這個數字是不是用過了,但這題可以接受數字重複使用

#3.但是他還是要控制往右去選,就是不回頭原則, 所以還是有start, 如果沒有 start 指標，每次都從頭選，你會算出 [2, 3, 2]；有了 start 且遞迴傳入 i，你只能選出 [2, 2, 3]

#4.這題不需要 if index == len(candidates)，因為只要 remain < candidates[i]，迴圈就會自動終止