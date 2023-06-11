"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        h1 = head
        
        while h1:
            node = Node(h1.val, None, None)
            node.next = h1.next
            h1.next = node
            h1 = node.next
                    
        h1 = head
        
        while h1:
            if h1.random:
                h1.next.random = h1.random.next
            else:
                h1.next.random = None
            h1 = h1.next.next

        h1 = head
        h2 = head.next
        temp = h2

        while h1:
            h1.next = h1.next.next
            if h2.next:
                h2.next = h2.next.next
            else:
                h2.next = None
            h1 = h1.next
            h2 = h2.next
        
        return temp
        