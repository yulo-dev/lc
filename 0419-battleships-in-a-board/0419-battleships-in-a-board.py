class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        rows = len(board)
        cols = len(board[0])
        count = 0

        for r in range(rows):
            for c in range(len(board[0])):
                # 1. 如果是海 ('.')，直接略過
                if board[r][c] == '.':
                    continue

                # 2. 檢查上方是否有船身
                # 如果你看到這格是 X，但「上一層樓 (r-1)」的「同一間房 (c)」也是 X
                # 代表這格只是某艘垂直戰艦的「身體」或「尾巴」。
                # 因為我們在處理上一層樓時，應該已經在那艘船的「頭」數過它了。所以這格我們不數，直接 continue
                if r > 0 and board[r-1][c] == 'X':
                    continue

                # 3. 檢查左方是否有船身
                # 如果你看到這格是 X，但「同一層樓 (r)」的「左邊那一間 (c-1)」也是 X
                # 代表這格是某艘水平戰艦的「身體」。因為這艘船的「頭」在左邊，我們之前已經數過了。所以這格也不數
                if c > 0 and board[r][c-1] == 'X':
                    continue

                count += 1

        return count


# 一個格子 board[r][c] 要成為一艘船的起點，必須滿足：
    #它本身是 'X'。
    #上方沒有 'X'：如果上方有 'X'，代表它是某艘垂直戰艦的「身子」。
    #左邊沒有 'X'：如果左邊有 'X'，代表它是某艘水平戰艦的「身子」。

# 程式透過排除法 把「船身」踢掉，最後只留下「船頭」
    # 如果你是水，直接 continue。能留下來的進入下一關的一定都是 X（戰艦的一部分）
    # 如果你這格是 X，但你「樓上」也是 X，代表你只是某艘直向戰艦的「下半部」。因為我們已經在處理樓上那一層時數過這艘船了，所以你被排除，直接 continue
    #如果你這格是 X，但你「左邊」也是 X，代表你只是某艘橫向戰艦的「右半部」。同樣地，左邊那一格早就被數過了，所以你也直接 continue
    
# 所以最後贏家就是
    # 當一個座標 (r, c) 經歷了這三層篩選都沒被 continue 掉，它必須同時滿足：
        # 它本身是 X。
        # 它的上方不是 X。
        # 它的左方不是 X。
        # 「垂直最上面的」或者是「水平最左邊的」