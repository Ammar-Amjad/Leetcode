class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        
        stack = deque([root])  
        
        while stack:
            prev = None
            
            for i in range(len(stack)):
                node = stack.popleft() 
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                
        return root