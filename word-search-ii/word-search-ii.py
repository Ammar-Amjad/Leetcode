class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

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
            
    def pruneWord(self, word):
        cur = self.root
        node_and_child_key = []

        for char in word:
            node_and_child_key.append((cur, char))

            if char in cur.children:
                cur = cur.children[char]
            else:
                raise ValueError(f'Character "{char}" not found in Trie')

        for node, char in reversed(node_and_child_key):
            if len(node.children[char].children) == 0:
                del node.children[char]
            else:
                break 



            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        res = set()
        visited = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(i, j, node, word): 
            
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visited or board[i][j] not in node.children:
                return 
            
            node = node.children[board[i][j]]
            word += board[i][j]
            
            if node.eow:
                res.add(word)
                node.eow = False
                trie.pruneWord(word)
                
            visited.add((i, j))
            
            for x, y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                dfs(i + x, j + y, node, word)
            
            visited.remove((i, j))
            
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie.root, "")
        return list(res)
        