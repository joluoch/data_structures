'''Letter Combinations of a Phone Number
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    Example:Input: digits = "23"
            Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''
def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            
            return []

        ans = ['']
        digitToLetters = ['', '', 'abc', 'def', 'ghi',
                          'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        for d in digits:
            temp = []
            for s in ans:
                for c in digitToLetters[ord(d) - ord('0')]:
                    temp.append(s + c)
            ans = temp

        return ans


'''search word one '''
def exist(board,word):

    row,col = len(board),len(board[0])
    path = set()

    def dfs(r,c,i):
        if i == len(word):
            return True
        
        if (r <0 or c<0 or
            r>=row or c>=col or
            word[i] != board[r][c]or
            (r,c) in path):
            return False

        path.add((r,c))

        res = (dfs(r+1,c,i+1) or
               dfs(r-1,c,i+1) or
               dfs(r,c+1,i+1) or
               dfs(r,c-1,i+1))
        path.remove((r,c))

        return res
    
    for r in range(row):
        for c in range(col):
            if (dfs(r,c,0)): return True
    
    return False
        