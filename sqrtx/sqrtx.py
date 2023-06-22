class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        L = 0
        R = x // 2
        
        while L <= R:
            M = (L + R) // 2
            Mval = M * M 
            
            if Mval > x:
                R = M - 1
            elif Mval < x:
                L = M + 1
            else:
                return M
        return R