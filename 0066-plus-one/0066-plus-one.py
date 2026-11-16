class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        cnt = 0
        tot = 0
        carry = 0
        res = []
        
        for i in range(len(digits)-1, -1, -1):

            if i == len(digits)-1:
                tot = digits[i] + 1
                
                cnt = tot % 10
                carry = tot // 10

                res.append(cnt)

            else:
                tot = digits[i] + carry

                cnt = tot % 10
                carry = tot // 10

                res.append(cnt)

        if carry:
            res.append(carry)
            
        return res[::-1]
