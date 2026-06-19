# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        n = 1
        leftprev = None
        final = head

        while n <= right:
            if n == left - 1:
                leftprev = head

            if n == left:
                leftmove = head
                prev = None
                while n <= right:
                    if n == right:
                        headupdate = leftmove.next
                    temp = leftmove.next
                    leftmove.next = prev
                    prev = leftmove
                    if n < right:
                        leftmove = temp
                    n += 1
                head.next = headupdate
                if leftprev:
                    leftprev.next = leftmove
                

            head = head.next
            n += 1

        if leftprev:
            return final
        else:
            return leftmove
