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
            return root
        
        queue = deque([(root, 0)])
        levels = []
        
        while queue:
            curr, level = queue.popleft()
            if level == len(levels):
                levels.append([])
                
            levels[level].append(curr.val)
            
            for c in curr.children:
                queue.append((c, level + 1))
                 
        return levels