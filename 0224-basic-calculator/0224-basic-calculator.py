class Solution:
    def calculate(self, s: str) -> int:
        
        stack = [] # 存外層狀態：先存 res 再存 sign（或反過來也行，但要一致）
        res = 0   # 目前這一層（目前括號層）已經算好的結果
        sign = 1 # 下一個數字要用 + 還是 - 加到 res（+1 或 -1）
        num = 0 # 正在讀的數字（可能是多位數）

        for ch in s:
            #1) 遇到數字：累積成多位數
            if ch.isdigit():
                num = num * 10 + int(ch) #int(ch)也可以用 ord(ch) - ord("0")取代

            #2) 遇到 + 或 -：把剛剛的 num 結算進 res
            elif ch in '+-':
                res += sign * num 
                num = 0 
                sign = 1 if ch == '+' else -1

            #3) 遇到 (：把外層狀態存起來，進新層
            elif ch == '(':
                stack.append(res) # Save current result and sign to stack
                stack.append(sign)
                res = 0 # Reset state for inner expression
                sign = 1

            #4) 遇到 )：把這層算完，然後跟外層合併
            elif ch == ')':
                res += sign * num 
                num = 0
                prev_sign = stack.pop() 
                prev_res = stack.pop() 
                res = prev_res + prev_sign * res

            # else: space -> ignore

        #字串結尾不會自動結算，所以最後要再加一次
        res += sign * num
        return res