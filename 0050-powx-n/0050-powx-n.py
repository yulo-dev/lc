class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #Binary Exponentiation（快速冪）
        #n 是偶數：直接把 x 平方，n 除以 2。
        #n 是奇數：先把一個 x 乘進 res，再把 x 平方、n 除以 2。

        res = 1

        if n < 0:
            x = 1/x
            n = -n

        while n > 0:
            if n % 2 == 1:
                res *= x

            x *= x
            n //= 2

        return res