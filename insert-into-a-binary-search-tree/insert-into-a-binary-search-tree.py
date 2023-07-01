# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root
        
        res = root
        while root:
            if val < root.val: 
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                root = root.left
                
            elif val > root.val:
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right
        return res