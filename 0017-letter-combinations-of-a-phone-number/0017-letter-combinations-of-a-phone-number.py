class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        res = []
        path = []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtracking(index, path):
            # 1. 終止條件：當路徑長度等於數字長度，代表湊齊了
            if len(path) == len(digits):
                res.append("".join(path)) # 字串不用 .copy()，因為 join 會產生新字串
                return

            # 2. 找出當前數字對應的所有字母
            current_digit = digits[index]
            letters = mapping[current_digit]

            for char in letters:
                # 做選擇
                path.append(char)
                # 探索：往「下一個數字」移動
                backtracking(index + 1, path)
                # 撤銷選擇
                path.pop()

        backtracking(0, [])
        return res
