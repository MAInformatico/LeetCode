class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
    
        primes = [False]*2 + [True]*(n-2)
        result = n - 2
        for i in range(2, math.ceil(math.sqrt(n))):
            if primes[i]:
                for j in range(i*i, n, i):
                    if primes[j]:
                        result -= 1
                        primes[j] = False
                        
        return result
