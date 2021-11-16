import collections

def openLock(self, deadends, target: str) -> int:
        nums = []
        deadends = set(deadends)
        
        if '0000' in deadends: return -1
        
        #bfs
        
        q = collections.deque([('0000',0)])
        
        visited = set()
        
        while q :
            cand,steps = q.popleft()
            if cand == target: return steps
            
            for i in range (4):
                for digit in [((int(cand[i])+1)%10),((int(cand[i])-1)%10)]:#moving up or down
                    nxt = cand[:i] + str(digit) + cand[i+1:]
                    if nxt not in deadends and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt,steps+1))
        return -1