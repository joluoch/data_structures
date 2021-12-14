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

'''wildcard matching 
    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).
'''

def isMatch(self, s: str, p: str) -> bool:
    s_len, p_len = len(s), len(p)
    s_idx = p_idx = 0
    star_idx = s_tmp_idx = -1
 
    while s_idx < s_len:
            # If the pattern character = string character
            # or pattern character = '?'
        if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
            s_idx += 1
            p_idx += 1
    
            # If pattern character = '*'
        elif p_idx < p_len and p[p_idx] == '*':
                # Check the situation
                # when '*' matches no characters
            star_idx = p_idx #save start position for possible back tracking 
            s_tmp_idx = s_idx # stringpointer
            p_idx += 1
                              
            # If pattern character != string character
            # or pattern is used up
            # and there was no '*' character in pattern 
        elif star_idx == -1:
            return False
                              
            # If pattern character != string character
            # or pattern is used up
            # and there was '*' character in pattern before
        else:
            # Backtrack: check the situation
            # when '*' matches one more character
            p_idx = star_idx + 1
            s_idx = s_tmp_idx + 1
            s_tmp_idx = s_idx
        
    # The remaining characters in the pattern should all be '*' characters
    return all(p[i] == '*' for i in range(p_idx, p_len))

'''regular expression matching 
    TIme : O(s.p)
    top-down dynamic programming  and memoization
'''
def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        
        def dfs(i,j):
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            if i >= len(s) and j >= len(p):
                return True
            
            if j>= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if (j+1) < len(p) and p[j+1] == '*':
                
                cache[(i,j)] = (dfs(i,j+2)or #dont use *
                                (match and dfs(i+1,j)))  #use it
                
                return cache[(i,j)]
            
            if match:
                
                cache [(i,j)] = dfs(i+1,j+1)
                
                return cache[(i,j)]
            cache[(i,j)] = False
            
            return False
        
        return dfs(0,0)