# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         if head is None or head.next is None:
#             return head
        
#         p = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return p
        if head is None:
            return head
        
        self.temp = None
        def dfs(root):
            if root.next is None: 
                self.temp = root 
                return root
            
            p = dfs(root.next)
            p.next = root 
            return root
        p = dfs(head)
        p.next = None
        return self.temp