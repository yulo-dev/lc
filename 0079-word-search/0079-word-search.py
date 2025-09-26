class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.check(board, i, j, 0, word, set()):
                    return True
        
        return False

    def check(self, board, x, y, k, word, visited):

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if board[x][y] != word[k]:
            return False # ← 字母不符合直接 return False, 因為這裡還沒加進 visited 所以不需要回溯

        if k == len(word) - 1:
            return True 
            
        visited.add((x, y))
        result = False

        # 本身字符合 就往他四個方向檢查
        for dir_x, dir_y in directions:
            new_x = x + dir_x
            new_y = y + dir_y
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if (new_x, new_y) not in visited:
                    if self.check(board, new_x, new_y, k + 1, word, visited):
                        result = True
                        break
            
        # 如果本身符合但後續的字不符合 那就要慢慢backtrack 把這些原本被放進visited的字拿掉
        visited.remove((x, y))
        return result