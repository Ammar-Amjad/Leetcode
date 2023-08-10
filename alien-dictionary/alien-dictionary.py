from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
 
        graph = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        # Step 2: Build graph and in-degree map
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_degree[c2] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""

        # Step 3: Kahn's algorithm for Topological Sort
        queue = deque([char for char, degree in in_degree.items() if degree == 0])
        result = []
        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check for Validity
        if len(result) != len(in_degree):
            return ""
        return ''.join(result)
