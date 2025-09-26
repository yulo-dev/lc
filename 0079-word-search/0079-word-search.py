class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(board, i, j, word, 0, set()):
                    return True
        return False  

    def check(self, board, x, y, word, k, visited):
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

        if board[x][y] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        visited.add((x, y))
        result = False # result 只是為了 中途存「有沒有找到成功路徑」 預設這條路會失敗

        for dir_x, dir_y in DIRECTIONS:
            new_x = x + dir_x
            new_y = y + dir_y
            
            if (0 <= new_x < len(board)) and (0 <= new_y < len(board[0])):
                if (new_x, new_y) not in visited:
                    if self.check(board, new_x, new_y, word, k + 1, visited):
                        result = True # 如果某個方向成功 → 把 result 改成 True，並 break 提前結束 把他往上傳
                        break

        visited.remove((x, y))
        return result