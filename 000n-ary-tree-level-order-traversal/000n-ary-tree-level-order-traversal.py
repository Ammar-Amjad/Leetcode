"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        self.res = []
        
        def dfs(node, level):
            if len(self.res) == level:
                self.res.append([])
            self.res[level].append(node.val)
            for c in node.children:
                dfs(c, level + 1)
        
        dfs(root, 0)
        return self.res
            