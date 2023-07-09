"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    head = None
    prev = None

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        
        self.helper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:
            self.head = node
        self.prev = node

        self.helper(node.right)