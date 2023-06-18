class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root  # If both nodes are found in left and right branches, then root is LCA
        elif left is not None:
            return left  # If one node is found in left branch
        else:
            return right  # If one node is found in right branch or None if neither are found
