# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head
        dummy = sentinel
        curr = head
        
        while curr:
            if curr.val == val:
                dummy.next = curr.next
                curr = curr.next
            else:        
                curr = curr.next
                dummy = dummy.next
        
        return sentinel.next