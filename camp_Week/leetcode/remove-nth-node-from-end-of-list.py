# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        


        ahead , back = head , head

        for i in range(n):
            ahead = ahead.next

        if(not ahead):
            return head.next

        while ahead.next:
            ahead = ahead.next
            back = back.next
        
        back.next = back.next.next
        
        return head

        
        