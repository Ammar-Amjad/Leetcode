# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        
        i = 1
        temp = head
        
        while temp.next:
            i += 1
            temp = temp.next
        temp.next = head
        
        tail = head
        
        for j in range(i - (k % i) - 1):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        
        return new_head
            
        
            