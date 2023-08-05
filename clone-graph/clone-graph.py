"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        seen = {}
        
        def dfs(curr):
            if curr in seen:
                return seen[curr]
            
            copy = Node(curr.val)
            seen[curr] = copy 
            
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))            
            
            return copy
        
        return dfs(node)  