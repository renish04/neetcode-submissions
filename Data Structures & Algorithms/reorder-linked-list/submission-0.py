# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        curr = head

        while first.next :
            if first.next.next is None:
                if first == curr:
                    first = first.next
                    continue
                temp = curr.next
                curr.next = first.next
                first.next.next = temp
                first.next = None
                curr = temp
                first = curr
            else:
                first = first.next
        
        
          
