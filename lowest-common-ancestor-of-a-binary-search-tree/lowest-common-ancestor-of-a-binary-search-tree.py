# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        Min = min(p.val, q.val)
        Max = max(p.val, q.val)
        
        while root:
            if root.val > Max:
                root = root.left
            elif root.val < Min:
                root = root.right
            else:
                return root
        return None
        