class TrieNode:
    def __init__(self):
        self.eow = False
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.words.append(word)
        node.eow = True
        
                
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie()
        n = len(words[0])
        
        for word in words:
            trie.insert(word)
        res = []
        
        def getwords(prefix):
            node = trie.root
            
            for c in prefix:
                if c not in node.children:
                    return []
                node = node.children[c]
            return node.words
                
        
        def backtrack(idx, cur_words):
            if idx == n:
                res.append(cur_words[:])
                return 
        
            prefix = ''.join(word[idx] for word in cur_words) 
        
            words = getwords(prefix)
            
            for word in words:
                cur_words.append(word)
                backtrack(idx + 1, cur_words)
                cur_words.pop()
            
        
        for word in words:
            backtrack(1, [word])
        
        return res
        
        
        