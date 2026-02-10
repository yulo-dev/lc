class Solution:
    def isHappy(self, n: int) -> bool:

        # 需要 seen 是因為：有些數永遠不會變成 1，它會進入一個「循環」，如果不記錄看過的值，while 就會 無限跑下去。
        # 所以一旦發現 n 曾經出現過，就代表進入死循環，再算下去也只會重複，可以直接回傳 False
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            total = 0

            for ch in str(n):
                d = ord(ch) - ord("0") 
                total += d * d

            n = total

        return n == 1