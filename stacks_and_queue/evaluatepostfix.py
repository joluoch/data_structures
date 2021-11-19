def evalRPN(tokens: List[str]) -> int:
        stack = [] #make a stack to hold the numberes and result calculation
        
        for char in tokens: #iterate through the tokens
            if char not in "+*-/": #if token is not an operator then it is a number so we add to stack
                stack.append(int(char))
            else: #if it is an operator then we pop the last two values from the stack and the left + right 
                r,l = stack.pop(),stack.pop()
                if char == "*":
                    stack.append(l*r)
                elif char == "/":
                    stack.append(int(float(l)/r))
                elif char == "+":
                    stack.append(l+r)
                elif char == "-":
                    stack.append(l-r)
        
        
        return stack [-1]

#explanation : https://www.youtube.com/watch?v=3wGTlsLnZE4&list=PLLOxZwkBK52Akgqf4oSWPOQO9ROWS_9rc&index=20 
