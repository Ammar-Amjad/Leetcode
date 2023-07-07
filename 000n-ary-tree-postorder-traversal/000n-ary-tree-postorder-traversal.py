"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        self.res = []
        
        def dfs(node):
            
            for n in node.children:
                dfs(n)
            self.res.append(node.val) 
        
        dfs(root)
        return self.res
        