# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Find mid point
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse 2nd half
        prev, slow, prev.next = slow, slow.next, None
        
        while slow:
            slow.next, prev, slow = prev, slow, slow.next 
            
        # compare
        fast, slow = head, prev
        while slow:
            if slow.val != head.val:
                return False
            slow, head = slow.next, head.next
        return True