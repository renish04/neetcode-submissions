# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        while head:
            if head.next is None:
                return False
            else:
                if head.next.val == 1001:
                    return True
                else:
                    head.val = 1001
                    head = head.next