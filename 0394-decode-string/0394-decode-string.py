class Solution:
    def decodeString(self, s: str) -> str:
        
        # numeric
        # alphabets
        # [
        # ]

        stack = []
        curr_alpha = ""
        curr_num = 0

        for ch in s:
            if ch.isalpha():
                curr_alpha += ch

            elif ch.isnumeric():
                curr_num = curr_num * 10 + int(ch)

            elif ch == "[":
                stack.append((curr_num, curr_alpha))
                curr_alpha = ""
                curr_num = 0
                
            else:
                time, alpha = stack.pop()
                curr_alpha = alpha + time * curr_alpha

        return curr_alpha
