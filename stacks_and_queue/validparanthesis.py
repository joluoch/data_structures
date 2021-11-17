def isValid(self, s: str) -> bool:
        stack = []
        
        closeToOpen = {')':'(',']':'[','}':'{'} # dictionarry mappin to avoid alot of if staements 
        
        for symbol in s :
            if symbol in closeToOpen:
                if stack and stack[-1] == closeToOpen[symbol]:
                    stack.pop()  #pop from stack if the top of the stack if equal to the key of in the dictionary
                else:
                    return False
            else:
                stack.append(symbol)
        return True if not stack else False
    
#https://www.youtube.com/watch?v=WTzjTskDFMg
# explanation using if statements for comparision : https://afteracademy.com/blog/check-for-balanced-parentheses-in-an-expression