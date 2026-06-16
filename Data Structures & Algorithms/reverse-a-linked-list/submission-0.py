# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = 0
        curr = None

        while head:
            curr = head
            head = head.next

            if prev == 0:
                curr.next = None
            else:
                curr.next = prev
            prev = curr
            print(head)
        head = curr
        print(head)
        return head
