'''contain microsoft questions : OTHER CARD'''
def singleNumber(self, nums: List[int]) -> int:
        
    s = set()
        
    for num in nums:
        if num in s :
            s.remove(num)
        else:
            s.add(num)
    return s.pop()


'''roman to integer '''
def romanToInt(self, s: str) -> int:
        
    roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000 }
    res = 0 
        
    for i in range(len(s)):
        if (i+1) < len(s) and roman[s[i]] < roman [s[i+1]]:
                
            res -= roman[s[i]]
        else:
            res+= roman[s[i]]
    return res 

'''Excel sheet column number '''
def titleToNumber(self, columnTitle: str) -> int:
        
        multiplier = 1
        column= 0 
        for i in range(len(columnTitle)-1,-1,-1):
            column += (ord(columnTitle[i]) - 64) * multiplier
            multiplier *=26
        
        return column

'''find the celebrity'''
def findCelebrity(self, n: int) -> int:
        
        candidate = 0

    # everyone knows the celebrity
        for i in range(1, n):
            if knows(candidate, i):
                
                candidate = i

        # candidate knows nobody and everyone knows the celebrity
        for i in range(n):
            if i < candidate and knows(candidate, i) or not knows(i, candidate):
                return -1
            if i > candidate and not knows(i, candidate):
                return -1

        return candidate
