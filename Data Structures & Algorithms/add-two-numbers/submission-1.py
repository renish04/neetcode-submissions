# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q = 0
        prev = None

        while l1 or l2 or q:
            if not l1:
                l1sum = 0
            else:
                l1sum = l1.val
            if not l2:
                l2sum = 0
            else:
                l2sum = l2.val

            add = l1sum + l2sum + q

            if add > 9:
                r = add % 10
                q = add // 10
                temp = ListNode(r, prev)
                
            else:
                temp = ListNode(add, prev)
                q = 0

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            prev = temp

        move = prev
        previous = None

        while move:
            ext = move.next
            move.next = previous
            previous = move
            move = ext


        return previous
        