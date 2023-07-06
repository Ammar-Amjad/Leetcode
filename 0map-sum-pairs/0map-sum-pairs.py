class TrieNode:
    def __init__(self, Sum = 0):
        self.children = defaultdict(TrieNode)
        self.sum = Sum
        
class MapSum:

    def __init__(self): 
        self.root = TrieNode()
        self.map = defaultdict(int)
        
    def insert(self, key: str, val: int) -> None:  
        diff = val - self.map.get(key, 0)
        node = self.root
        for c in key:
            node = node.children[c]
            node.sum += diff
        self.map[key] = val
        
    def sum(self, prefix: str) -> int: 
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.sum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)