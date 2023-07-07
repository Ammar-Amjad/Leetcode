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
        
        stack = [root]
        res = []
        
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
            for c in node.children:
                stack.append(c)

        return res[::-1]
                
        