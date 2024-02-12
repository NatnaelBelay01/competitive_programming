# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        ptr1 = ListNode(0 , head)
        ptr2 = head
        head = ptr1

        while(ptr2):
            if(ptr2.val == val):
                while(ptr2 and ptr2.val == val):
                    ptr2 = ptr2.next
                ptr1.next = ptr2
                if(ptr2):
                    ptr2 = ptr2.next
                if(ptr1.next):
                    ptr1 = ptr1.next
                continue
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        return head.next


        