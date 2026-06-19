"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        rev = head
        prev = None

        while rev:
            temp1 = rev.next
            rev.next = prev
            prev = rev
            rev = temp1

        previous = None

        endmain = prev
        mapp ={}
        
        while prev:
            temp = Node(prev.val, previous, None)
            mapp[prev] = temp
            previous = temp
            prev = prev.next
        
        endprev = None

        while endmain:
            temp1 = endmain.next
            endmain.next = endprev
            endprev = endmain
            endmain = temp1     

        ranhead = previous
        final = previous
        
        while head:
            if head.random is None:
                ranhead.random = None
            else:
                x = head.random
                ranhead.random = mapp[x]

            head = head.next
            ranhead = ranhead.next

        return final