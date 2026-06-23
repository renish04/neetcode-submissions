# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            tail = list1
        else:
            tail = list2

        head = tail

        while list1 or list2:
            if tail == list1:
                if tail.next and tail.next.val < list2.val:
                    tail = tail.next
                    list1 = tail
                else:
                    list1 = list1.next
                    tail.next = list2
                    tail = list2
            
            elif tail == list2:
                if tail.next and tail.next.val < list1.val:
                    tail = tail.next
                    list2 = tail
                else:
                    list2 = list2.next
                    tail.next = list1
                    tail = list1
        return head




