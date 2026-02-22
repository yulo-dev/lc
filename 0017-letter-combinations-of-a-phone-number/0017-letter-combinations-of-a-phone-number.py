class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        path = []

        def backtracking(index, path): # index 告訴我：現在看第幾個數字
            if len(path) == len(digits):
                res.append("".join(path))
                return

            current_num = digits[index]
            letter = mapping[current_num] # 拿到這個數字的所有字母（例如 'abc'）

            for c in letter: # 「橫向」嘗試：選 a, 還是 b, 還是 c?
                path.append(c)

                # 「縱向」深入：不管我選了 a 還是 b，
                # 下一步都一定是去處理「下一個數字按鍵」(index + 1)
                backtracking(index+1, path)
                path.pop()

        backtracking(0, [])
        return res

#index (縱向/深度)：代表「現在輪到第幾個數字按鍵了？」（例如：先按 2，再按 3）。
#for loop (橫向/寬度)：代表「這個按鍵對應的字母，我要選哪一個？」（例如：按 2 時，選 'a'、'b' 還是 'c'？）