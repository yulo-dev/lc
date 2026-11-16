class Solution:
    def countPrimes(self, n: int) -> int:

        #2是質數 但題目是問比他小的 所以是0,1 都不是質數
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5)+1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)
