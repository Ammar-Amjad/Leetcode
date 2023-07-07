"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        def dfs(node, depth):
            level = []
            for c in node.children:
                level.append(dfs(c, depth + 1))
            if not node.children:
                return depth
            return max(level)
            
        
        return dfs(root, 1)
        