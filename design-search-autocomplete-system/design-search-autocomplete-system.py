import heapq
class TrieNode:
    def __init__(self, score = 0): 
        self.sentences = defaultdict(int)
        self.children = {}

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.heap = []
        self.sen = ''

        for i in range(len(sentences)):
            self.add_to_trie(sentences[i], times[i])

        self.cur_sentence = []
        self.cur_node = self.root
        self.dead = TrieNode()

    def input(self, c: str) -> List[str]:  
        if c == '#':
            cur_sentence = ''.join(self.cur_sentence)
            self.add_to_trie(cur_sentence, 1)
            self.cur_sentence = []
            self.cur_node = self.root
            return []
        
        self.cur_sentence.append(c)
        if c not in self.cur_node.children:
            self.cur_node = self.dead
            return []
        
        self.cur_node = self.cur_node.children[c]
        items = [(val, key) for key, val in self.cur_node.sentences.items()]
        ans = heapq.nsmallest(3, items)
        return [item[1] for item in ans]
    
    def add_to_trie(self, sentence, count):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentences[sentence] -= count
            

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)