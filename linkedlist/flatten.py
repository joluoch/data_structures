class Soltion:
    def flatten(self,head):
        if head != None:
            self.flatten_rec(head)
            return head
    def flatten_rec(self,head):
        curr,tail = head,head
        while curr != None:
            child = curr.child
            next = curr.next
            if child != None:
                tail = self.flatten_rec(child)
                tail.next = next
                if next !=None:
                    next.prev = tail
                    curr.next = child
                    child.prev = curr
                    curr.child = None
                    curr = tail
                else:
                    curr = next
                if curr!= None:
                    tail = curr
        return tail 