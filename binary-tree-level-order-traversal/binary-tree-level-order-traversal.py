# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []

        def dfs(node, level):
            if not node:
                return
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)


        dfs(root, 0)
        return levels