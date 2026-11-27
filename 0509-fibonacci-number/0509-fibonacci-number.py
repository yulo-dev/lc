class Solution:
    def fib(self, n: int) -> int:
        #base case
        if n <= 0 :
            return n
        
        dp_first = 0
        dp_second = 1


        for i in range(2, n+1):
            dp_update = dp_first + dp_second

            dp_first = dp_second
            dp_second = dp_update
            
            
        return dp_second