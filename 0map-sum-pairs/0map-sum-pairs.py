class TrieNode:
    def __init__(self, count = 0):
        self.count = count
        self.children = {}

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.keys = {}        

    def insert(self, key: str, val: int) -> None: 
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val

        node = self.root
        node.count += delta

        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += delta
        
    def sum(self, prefix: str) -> int:
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        return node.count    


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)