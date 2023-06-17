# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if node is None:
                return depth
            
            lv = dfs(node.left, depth + 1)
            rv = dfs(node.right, depth + 1)
            depth = max(lv, rv)
            
            return depth
        
        return dfs(root, 0)