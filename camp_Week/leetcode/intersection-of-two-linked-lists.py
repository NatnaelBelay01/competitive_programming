# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        dum = headA
        counta = 0
        while(dum):
            counta += 1
            dum = dum.next
        
        
        dum = headB
        countb = 0
        while(dum):
            countb += 1
            dum = dum.next
        
        ahead = headA
        while(counta > countb):
            ahead = ahead.next
            counta -= 1
        
        bhead = headB
        while(countb > counta):
            bhead = bhead.next
            countb -=1
        
        while(ahead and bhead):
            if ahead == bhead:
                return ahead
            ahead = ahead.next
            bhead = bhead.next

