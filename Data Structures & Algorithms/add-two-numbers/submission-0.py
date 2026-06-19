# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""

        while l1:
            str1 = str(l1.val) + str1
            l1 = l1.next

        while l2:
            str2 = str(l2.val) + str2
            l2 = l2.next
        
        summ = int(str1) + int(str2)

        strsum = str(summ)

        prev = None
        for i in range(len(strsum)):
            temp = ListNode(int(strsum[i]), prev)
            prev = temp
        
        return prev