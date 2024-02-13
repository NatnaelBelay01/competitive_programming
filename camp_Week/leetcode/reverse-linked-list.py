# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dum = head
        if head:
            head = head.next
            dum.next = None

        while head:
            temp = head
            head = head.next
            temp.next = dum
            dum = temp
        return dum
