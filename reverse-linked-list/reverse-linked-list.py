# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        t = None
        h1 = head
        h2 = head.next
        
        while h2:
            h1.next = t
            t = h1
            h1 = h2
            h2 = h2.next
        h1.next = t
        head = h1
        
        return head