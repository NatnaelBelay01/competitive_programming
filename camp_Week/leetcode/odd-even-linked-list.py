# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not(head) or not(head.next) or not(head.next.next)):
            return head
        fast = head.next
        slow = head

        while fast:

            if(fast.next):
                temp = fast.next
                if fast.next.next:
                    fast.next = fast.next.next
                    fast  = fast.next
                else:
                    fast.next = None
                    fast = None
                temp2 = slow.next
                slow.next = temp
                temp.next = temp2
                slow = slow.next
                
            else:
                break
        
        return head