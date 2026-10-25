class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = [] #(string, num)

        string = ""
        nums = 0

        for ch in s:
            if ch.isdigit():
                nums = nums * 10 + int(ch)

            elif ch == "[":
                stack.append((string, nums))

                string = ""
                nums = 0
                
            elif ch == "]":
                prev, times = stack.pop()
                string = prev + string * times

            else:
                string += ch

        return string