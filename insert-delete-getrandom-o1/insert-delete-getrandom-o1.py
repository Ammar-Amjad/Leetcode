class RandomizedSet:

    def __init__(self): 
        self.dic = {}
        self.arr = []
        
    def insert(self, val: int) -> bool: 
        idx = len(self.arr)
        if val not in self.dic:
            self.arr.append(val)
            self.dic[val] = idx
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool: 
        if val in self.dic:
            idx = self.dic[val]
            self.dic[self.arr[-1]] = idx
            self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
            del self.dic[val]
            self.arr.pop()
            return True
        else:
            return False
            
        
    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()