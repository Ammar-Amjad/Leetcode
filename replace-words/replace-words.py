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
        prefix = ''
        
        for char in word:  
            if char not in node.children: 
                # If a character isn't in the Trie, return the original word
                return word
            node = node.children[char] 
            prefix += char
            if node.eow:
                # If this is the end of a dictionary word, return the prefix found so far
                return prefix
        # If no shorter replacement was found, return the original word
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
            
            