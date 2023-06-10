# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        first = head
        sec = head.next
        dummy = head.next
        
        while sec and sec.next:
            first.next = sec.next
            first = first.next
            sec.next = first.next
            sec = sec.next
        
        first.next = dummy
        return head