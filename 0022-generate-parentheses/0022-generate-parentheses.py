class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        path = []
        
        # left: 已放了幾個 (
        # right: 已放了幾個 )
        def backtrack(left, right):
            # 1. 終止條件：括號放滿了 (長度達到 2n)
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            # 2. 選擇一：嘗試放左括號
            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop() # 回溯
                
            # 3. 選擇二：嘗試放右括號
            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop() # 回溯
        
        backtrack(0, 0)
        return res