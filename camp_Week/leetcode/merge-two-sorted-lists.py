# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = list1
        second = list2
        dummy = new = ListNode(-1)

        while(first or second):

            if(not first):
                new.next = second
                second = second.next
                new = new.next
            elif(not second):
                new.next = first
                first = first.next
                new = new.next

            elif(first.val == second.val):
                new.next = first
                first = first.next                
                new = new.next
                new.next = second
                new = new.next
                second = second.next
                
            elif(first.val < second.val):
                new.next = first
                first = first.next                
                new = new.next
            else:
                new.next = second
                second = second.next
                new = new.next

                
        return dummy.next
 