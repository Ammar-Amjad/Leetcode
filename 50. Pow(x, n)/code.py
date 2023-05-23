class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = abs(n)
            x = 1/x

        def rec(x, n):
            if n == 1:
                return x            
            elif n == 2:
                return x * x

            res = rec(x, n//2)

            if n % 2 == 0:
                return res * res
            else:
                return res * res * x
        
        return rec(x, n)