class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(x, y, k):
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
                        if check(new_x, new_y, k + 1):
                            result = True
                            break
            
            visited.remove((x, y))
            return result

        m, n = len(board), len(board[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if check(i, j, 0):
                    return True
        
        return False