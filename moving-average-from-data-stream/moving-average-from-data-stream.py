class MovingAverage:

    def __init__(self, size: int):
        self.queue = [0 for _ in range(size)]
        self.tail = 0
        self.curlen = 0
        self.size = size
        self.Sum = 0

    def next(self, val: int) -> float:
        if self.curlen >= self.size:
            self.Sum -= self.queue[self.tail % self.size]
        self.queue[self.tail % self.size] = val
        self.Sum += val
        self.tail += 1
        if self.curlen < self.size:
            self.curlen += 1
        return self.Sum / self.curlen if self.curlen != 0 else 0
    
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)