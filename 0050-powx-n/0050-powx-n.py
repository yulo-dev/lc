class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #Binary Exponentiation（快速冪）
        #n 是偶數：直接把 x 平方，n 除以 2。
        #n 是奇數：先把一個 x 乘進 res，再把 x 平方、n 除以 2。

        res = 1.0

        #negative = n < 0 
        if n < 0:
            negative = True
        else:
            negative = False

        n = abs(n)


        while n > 0:
            
            # odd
            if n % 2 == 1:
                res *= x

            x *= x
            n //= 2 
        
        return 1/res if negative else res