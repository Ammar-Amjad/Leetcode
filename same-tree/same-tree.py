# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = deque([(p, q)])
        
        def check(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return True
        
        while queue:
            p, q = queue.popleft()
            
            if not check(p, q):
                return False 
            if p:
                queue.append((p.right, q.right))
                queue.append((p.left, q.left))
        return True