# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        dum = ListNode()
        dum.next = head

        fast = dum
        slow = dum

        while(fast.next):
            if(fast.next.val < x):
                temp = fast.next
                fast.next = fast.next.next
                temp2 = slow.next
                slow.next = temp
                temp.next = temp2
                if(slow == fast):
                    fast = fast.next
                slow = slow.next
                continue
            fast = fast.next
        return dum.next


        