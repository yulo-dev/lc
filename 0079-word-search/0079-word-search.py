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
            return False
        if k == len(word) - 1:
            return True
            
        visited.add((x, y))
        result = False

        for dir_x, dir_y in directions:
            new_x = x + dir_x
            new_y = y + dir_y
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]):
                if (new_x, new_y) not in visited:
                    if self.check(board, new_x, new_y, k + 1, word, visited):
                        result = True
                        break
            
        visited.remove((x, y))
        return result