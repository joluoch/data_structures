
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(-1)
        dummy.next = head
        cur = head
    
        # stage one, interweave
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        cur = head
        
        # stage two ,update random
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = dummy
        old = head
        # stage three, remove old nodes
        while old:
            cur.next = old.next
            cur = old
            old = cur.next
        return dummy.next

#https://www.youtube.com/watch?v=g7U-FPBR_gQ 
        