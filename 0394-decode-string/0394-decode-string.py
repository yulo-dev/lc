class Solution:
    def decodeString(self, s: str) -> str:
        
        stack_ch = []
        stach_num = []

        curr_ch = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == "[":
                stack_ch.append(curr_ch)
                stach_num.append(curr_num)
                curr_ch = ""
                curr_num = 0
            elif ch == "]":
                prev_ch = stack_ch.pop()
                repeat_time = stach_num.pop()
                curr_ch = prev_ch + repeat_time * curr_ch
            else:
                curr_ch = curr_ch + ch

        return curr_ch