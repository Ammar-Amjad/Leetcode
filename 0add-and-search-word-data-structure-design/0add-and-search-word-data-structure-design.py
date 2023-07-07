class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
                
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.eow = True

    def search(self, word: str) -> bool:
        
        def dfs(Node, Word): 
            if not Word:
                if Node.eow:
                    return True
                else:
                    return False
                
            c = Word[0]
            
            if c == '.':
                for k in Node.children:
                    if dfs(Node.children[k], Word[1:]):
                        return True
            elif c in Node.children:
                if dfs(Node.children[c], Word[1:]):
                    return True
            return False
        
        return dfs(self.root, word) 

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)