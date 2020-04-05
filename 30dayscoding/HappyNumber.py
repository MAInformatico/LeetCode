class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s: return False
            s.add(n)
            sumN = 0
            while n:
                sumN += (n % 10) ** 2
                n //= 10
            n = sumN
        return n == 1
