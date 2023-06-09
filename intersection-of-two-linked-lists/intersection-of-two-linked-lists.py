# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        PA = headA
        PB = headB
        
        while PA != PB:
            if PA is None:
                PA = headB
            else:
                PA = PA.next
            if PB is None:
                PB = headA
            else:
                PB = PB.next
        return PA