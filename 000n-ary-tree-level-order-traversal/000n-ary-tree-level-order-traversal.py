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
        
        stack = [(root, 0)] 
        level = []
        
        while stack:
            node, idx = stack.pop()
            for n in node.children[::-1]:
                stack.append((n, idx + 1))
            
            if len(level) <= idx:
                level.append([node.val])
            else:
                level[idx] += [node.val]
                
        return level            
            