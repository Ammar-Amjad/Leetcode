class MyQueue:

    def __init__(self):
        self.queToStack = []

    def push(self, x: int) -> None:
        self.queToStack.append(x)
        return None

    def pop(self) -> int:
        if self.empty():
            return -1
        
        secStack = []
        while self.queToStack:
            secStack.append(self.queToStack.pop())
        
        res = secStack.pop()
        while secStack:
            self.queToStack.append(secStack.pop())
        
        return res
        

    def peek(self) -> int:
        return self.queToStack[0]

    def empty(self) -> bool:
        return len(self.queToStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()