# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, parent):
            if not node:
                return True
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            if left and right:
                self.ans += 1
            return left and right and node.val == parent

        dfs(root, None)
        return self.ans