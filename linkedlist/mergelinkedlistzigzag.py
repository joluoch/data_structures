 def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head
 
        # swap their positions until one finishes off
        while p_curr != None and q_curr != None:
 
            # Save next pointers
            p_next = p_curr.next
            q_next = q_curr.next
 
            # make q_curr as next of p_curr
            q_curr.next = p_next  # change next pointer of q_curr
            p_curr.next = q_curr  # change next pointer of p_curr
 
            # update current pointers for next iteration
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr