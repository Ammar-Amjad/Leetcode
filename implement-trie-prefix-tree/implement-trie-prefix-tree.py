class TrieNode:
    
    def __init__(self):
        self.eow = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:
            idx = ord(c) - ord('a')
            
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            
            node = node.children[idx] 
        node.eow = True 
                
              
    def search(self, word: str) -> bool:
        node = self.root
        
        for c in word:
            idx = ord(c) - ord('a') 
            if node.children[idx] == None:
                return False
            node = node.children[idx]
        return node.eow
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for c in prefix:
            idx = ord(c) - ord('a')
            
            if node.children[idx] == None:
                return False
            node = node.children[idx]
        return True 
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)