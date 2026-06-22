# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        stale = dummy

        looper = 0
        checker = head

        while checker:
            looper += 1
            checker = checker.next

        groups = looper // k
        groups_made = 0

        curr = head
        prev = None

        while groups_made < groups:
            n = 0
            head = curr

            while n < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                n += 1

            stale.next = prev
            stale = head
            prev = None
            groups_made += 1
        
        if curr:
            stale.next = curr

        return dummy.next


