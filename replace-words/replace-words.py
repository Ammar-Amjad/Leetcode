class TrieNode:
    def __init__(self):
        self.eow = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.eow = True        
        
    def startsWith(self, word):
        node = self.root
        res = ''
        
        for c in word:  
            if c not in node.children: 
                return word
            node = node.children[c] 
            res += c
            if node.eow == True:
                return res
                
        return word
        
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        
        for d in dictionary:
            trie.insert(d)
        
        result = []
        for s in sentence.split(' '):
            result.append(trie.startsWith(s))
        return ' '.join(result)
            
            