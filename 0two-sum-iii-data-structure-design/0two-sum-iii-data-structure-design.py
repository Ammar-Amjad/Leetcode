class TwoSum:

    def __init__(self):
        self.dic = {}
        
    def add(self, number: int) -> None:
        if number not in self.dic:
            self.dic[number] = 1
        else:
            self.dic[number] += 1

    def find(self, value: int) -> bool:
        
        for n in self.dic.keys():
            val = value - n
            if n != val:
                if val in self.dic:
                    return True
            elif self.dic[n] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)