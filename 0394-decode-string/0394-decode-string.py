class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []

        for ch in s:
            if ch.isdigit() or ch.isalpha() or ch == "[":
                stack.append(ch)

            elif ch == "]":

                #處理中括號裡面的字串們
                words = ""
                while stack and stack[-1] != "[":
                    word = stack.pop()
                    words = word + words

                #這是在pop "["
                stack.pop()

                #處理前面的數字
                total_time = ""
                while stack and stack[-1].isdigit():
                    time = stack.pop()
                    total_time = time + total_time

                #串在一起 然後放回stack 因為他可能是nested list 等下還會拿這結果去乘以別的
                decode = words * int(total_time)
                stack.append(decode)
                    
        return "".join(stack)