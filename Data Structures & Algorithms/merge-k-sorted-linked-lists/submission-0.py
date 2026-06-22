# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        looper = 0

        for x in range(len(lists)):
            head = lists[x]
            while head:
                looper += 1
                head = head.next
            
        for j in range(looper):
            mini = float('inf')
            corr_list = None

            for i in range(len(lists)):
                if lists[i] and lists[i].val < mini:
                    mini = lists[i].val
                    corr_list = i
            
            tail.next = lists[corr_list]
            tail = lists[corr_list]
            lists[corr_list] = lists[corr_list].next

        return dummy.next

