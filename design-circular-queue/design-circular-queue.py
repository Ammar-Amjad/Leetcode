class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.head = 0
        self.tail = 0
        self.len = k
        self.curlen = 0

    def enQueue(self, value: int) -> bool:
        print(self.queue)
        if not self.isFull():
            self.queue[self.tail % self.len] = value
            self.tail = self.tail + 1
            self.curlen += 1
            
            return True
        return False
    
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.head + 1
            self.curlen -= 1
            return True
        return False

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head % self.len]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.tail - 1) % self.len]

    def isEmpty(self) -> bool:
        return self.curlen == 0

    def isFull(self) -> bool:
        return self.curlen == self.len
            

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()