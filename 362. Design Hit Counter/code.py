from collections import deque
class HitCounter:

    def __init__(self):
        self.counter = deque()

    def hit(self, timestamp: int) -> None:
        self.counter.append(timestamp)        

    def getHits(self, timestamp: int) -> int:
        while self.counter and timestamp - self.counter[0] >= 300:
            self.counter.popleft()
        return len(self.counter)