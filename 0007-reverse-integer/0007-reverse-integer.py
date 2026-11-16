class Solution:
    def reverse(self, x: int) -> int:
        
        str_x = str(x)
        res = []

        for i in range(len(str_x)-1, -1, -1):
            if str_x[i] != "-":
                res.append(str_x[i])

        result = int(''.join(res))
            
        if x < 0:
            result *= -1

        if result > 2 ** 31 -1 or result < -(2 ** 31):
            return 0
        
        return result



            