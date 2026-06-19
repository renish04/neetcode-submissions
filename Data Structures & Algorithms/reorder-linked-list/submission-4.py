# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast:
            if fast.next is None or fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left = head
        right = prev

        while left.next:
            templ = left.next
            tempr = right.next
            left.next = right
            right.next = templ
            left = templ
            right = tempr
        
        left.next = right
        right.next = None
        

