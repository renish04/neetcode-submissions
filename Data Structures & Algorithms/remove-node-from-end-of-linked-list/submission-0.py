# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        trace = dummy 
        x = 1

        while trace.next:
            trace = trace.next 
            x += 1

        curr = dummy
        m = 0

        while curr:
            if m == (x-n)-1:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
                m += 1
            
        return dummy.next
        
        
