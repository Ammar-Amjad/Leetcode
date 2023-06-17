# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return  0
        
        levels = []
        queue = deque([root])
        depth = 0
        
        while queue:
            levels.append([])
            
            for i in range(len(queue)):
                node = queue.popleft()
                
                levels[depth].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth