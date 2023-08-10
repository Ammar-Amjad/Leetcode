from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adj_list = defaultdict(list)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj_list[c1]:
                        adj_list[c1].append(c2)
                        in_degree[c2] += 1
                    break
            else:
                if len(w1) > len(w2):
                    return ''
                
        queue = deque()

        for c in in_degree:
            if in_degree[c] == 0:
                queue.append(c)

        res = []
        while queue:
            node = queue.popleft()
            res.append(node)

            for nei in adj_list[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return ''.join(res) if len(res) == len(in_degree) else ''
                
                
                