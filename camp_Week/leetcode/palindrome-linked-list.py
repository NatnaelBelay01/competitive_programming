# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        new = ListNode()

        dum = head
        
        while(dum):
            new.val = dum.val
            dum = dum.next
            if(dum):
                temp = ListNode()
                temp.next = new
                new = temp

        first , second = head , new




        while(first and second):
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True 
        