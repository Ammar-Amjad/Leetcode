# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = Queue()
        q.put(root)
        q.put(root)

        while not q.empty():
            t1 = q.get()
            t2 = q.get()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            q.put(t1.left)
            q.put(t2.right)
            q.put(t1.right)
            q.put(t2.left)
        return True