class Solution:
    def romanToInt(self, s: str) -> int:
        #create a map
        #iterate through s

        mapping = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0

        for i, ch in enumerate(s):
            if i > 0 and (ch == "V" or ch == "X") and s[i-1] == "I":
                sum -= 2
            if i > 0 and (ch == "L" or ch == "C") and s[i-1] == "X":
                sum -= 20
            if i > 0 and (ch == "D" or ch == "M") and s[i-1] == "C":
                sum -= 200
            
            sum += mapping[ch]
        
        return sum
            