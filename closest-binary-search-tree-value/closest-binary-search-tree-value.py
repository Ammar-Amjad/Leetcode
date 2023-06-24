# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
        
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.res = float('inf')
        def dfs(node):
            if node is None:
                return None
            
            Val = abs(node.val - target)
            OVal = abs(self.res - target) 
            if Val == OVal and node.val < self.res:
                self.res = node.val
            elif Val < OVal:
                self.res = node.val
            dfs(node.left)
            dfs(node.right)
            
        dfs(root) 
        return self.res