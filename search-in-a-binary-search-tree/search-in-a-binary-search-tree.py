# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if node is None:
                return None
            A = None
            B = None
            if node.val == val:
                return node
            elif val < node.val:
                A = dfs(node.left)
            elif val > node.val:
                B = dfs(node.right)
            return A if A is not None else B
        return dfs(root)