class Solution:
    def __init__(self):
        self.cache = {}
        
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n in self.cache:
            return self.cache[n]
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
        
        self.cache[n] = result
        
        return result